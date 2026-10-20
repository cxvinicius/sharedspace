from datetime import datetime, timedelta, timezone
from uuid import UUID, uuid4

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import delete, select

from app.database.connection import SessionLocal
from app.enums.event_type import EventType
from app.enums.session_status import SessionStatus
from app.main import app
from app.persistence.models.event import EventModel
from app.persistence.models.session import SessionModel
from app.persistence.models.space import SpaceModel
from app.services.session_lifecycle import SessionLifecycleService


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def test_space():
    space_id = uuid4()
    db = SessionLocal()

    db.add(
        SpaceModel(
            id=space_id,
            name="Test Space",
            description="Automated test space",
            capacity=5,
        )
    )
    db.commit()
    db.close()

    yield space_id

    db = SessionLocal()

    session_ids = db.scalars(
        select(SessionModel.id).where(
            SessionModel.space_id == space_id
        )
    ).all()

    if session_ids:
        db.execute(
            delete(EventModel).where(
                EventModel.session_id.in_(session_ids)
            )
        )
        db.execute(
            delete(SessionModel).where(
                SessionModel.id.in_(session_ids)
            )
        )

    db.execute(
        delete(SpaceModel).where(SpaceModel.id == space_id)
    )

    db.commit()
    db.close()


def test_check_in_creates_active_session_and_event(client, test_space):
    response = client.post(f"/spaces/{test_space}/sessions")

    assert response.status_code == 201

    data = response.json()

    assert data["space_id"] == str(test_space)
    assert data["status"] == SessionStatus.ACTIVE.value

    started_at = datetime.fromisoformat(
        data["started_at"].replace("Z", "+00:00")
    )
    expires_at = datetime.fromisoformat(
        data["expires_at"].replace("Z", "+00:00")
    )

    assert expires_at - started_at == timedelta(minutes=30)

    db = SessionLocal()
    try:
        event = db.scalar(
            select(EventModel).where(
                EventModel.session_id == UUID(data["id"]),
                EventModel.type == EventType.CHECK_IN.value,
            )
        )
        assert event is not None
    finally:
        db.close()


def test_check_out_completes_session(client, test_space):
    check_in = client.post(f"/spaces/{test_space}/sessions")
    session_id = check_in.json()["id"]

    response = client.post(f"/sessions/{session_id}/checkout")

    assert response.status_code == 200
    assert response.json()["status"] == SessionStatus.COMPLETED.value
    assert response.json()["ended_at"] is not None

    db = SessionLocal()
    try:
        event = db.scalar(
            select(EventModel).where(
                EventModel.session_id == UUID(session_id),
                EventModel.type == EventType.CHECK_OUT.value,
            )
        )
        assert event is not None
    finally:
        db.close()


def test_confirmation_renews_session(client, test_space):
    check_in = client.post(f"/spaces/{test_space}/sessions")
    session_id = UUID(check_in.json()["id"])

    db = SessionLocal()
    try:
        session = db.get(SessionModel, session_id)
        session.status = SessionStatus.CONFIRMATION_PENDING.value
        session.confirmation_requested_at = datetime.now(timezone.utc)
        session.expires_at = datetime.now(timezone.utc) + timedelta(
            minutes=5
        )
        db.commit()
    finally:
        db.close()

    response = client.post(f"/sessions/{session_id}/confirm")

    assert response.status_code == 200
    assert response.json()["status"] == SessionStatus.ACTIVE.value

    db = SessionLocal()
    try:
        event = db.scalar(
            select(EventModel).where(
                EventModel.session_id == session_id,
                EventModel.type == EventType.RENEWAL.value,
            )
        )
        assert event is not None
    finally:
        db.close()


def test_expired_session_is_auto_terminated(test_space):
    db = SessionLocal()

    try:
        session_id = uuid4()
        now = datetime.now(timezone.utc)

        db.add(
            SessionModel(
                id=session_id,
                space_id=test_space,
                status=SessionStatus.ACTIVE.value,
                started_at=now - timedelta(minutes=31),
                expires_at=now - timedelta(minutes=1),
                confirmation_requested_at=None,
                ended_at=None,
            )
        )
        db.commit()
    finally:
        db.close()

    lifecycle = SessionLifecycleService()
    lifecycle.process_expirations()

    db = SessionLocal()
    try:
        session = db.get(SessionModel, session_id)
        assert session.status == SessionStatus.CONFIRMATION_PENDING.value

        # Simulate the five-minute confirmation window expiring.
        session.expires_at = datetime.now(timezone.utc) - timedelta(
            seconds=1
        )
        db.commit()
    finally:
        db.close()

    lifecycle.process_expirations()

    db = SessionLocal()
    try:
        session = db.get(SessionModel, session_id)

        assert session.status == SessionStatus.AUTO_TERMINATED.value
        assert session.ended_at is not None

        event = db.scalar(
            select(EventModel).where(
                EventModel.session_id == session_id,
                EventModel.type == EventType.AUTO_TERMINATION.value,
            )
        )
        assert event is not None
    finally:
        db.close()


def test_capacity_cannot_be_exceeded(client, test_space):
    for _ in range(5):
        response = client.post(f"/spaces/{test_space}/sessions")
        assert response.status_code == 201

    response = client.post(f"/spaces/{test_space}/sessions")

    assert response.status_code == 409
    assert response.json()["detail"] == "Space capacity has been reached."


def test_occupancy_is_zero_when_space_is_empty(client, test_space):
    response = client.get(f"/spaces/{test_space}/occupancy")

    assert response.status_code == 200
    assert response.json() == {
        "space_id": str(test_space),
        "capacity": 5,
        "occupied": 0,
        "available": 5,
    }


def test_occupancy_counts_active_sessions(client, test_space):
    for _ in range(3):
        response = client.post(f"/spaces/{test_space}/sessions")
        assert response.status_code == 201

    response = client.get(f"/spaces/{test_space}/occupancy")

    assert response.status_code == 200
    assert response.json()["capacity"] == 5
    assert response.json()["occupied"] == 3
    assert response.json()["available"] == 2


def test_occupancy_includes_confirmation_pending_sessions(
    client,
    test_space,
):
    check_in = client.post(f"/spaces/{test_space}/sessions")
    session_id = UUID(check_in.json()["id"])

    db = SessionLocal()

    try:
        session = db.get(SessionModel, session_id)
        session.status = SessionStatus.CONFIRMATION_PENDING.value
        db.commit()
    finally:
        db.close()

    response = client.get(f"/spaces/{test_space}/occupancy")

    assert response.status_code == 200
    assert response.json()["occupied"] == 1
    assert response.json()["available"] == 4


def test_occupancy_reports_full_capacity(client, test_space):
    for _ in range(5):
        response = client.post(f"/spaces/{test_space}/sessions")
        assert response.status_code == 201

    response = client.get(f"/spaces/{test_space}/occupancy")

    assert response.status_code == 200
    assert response.json()["capacity"] == 5
    assert response.json()["occupied"] == 5
    assert response.json()["available"] == 0


def test_occupancy_returns_404_for_missing_space(client):
    missing_space_id = uuid4()

    response = client.get(
        f"/spaces/{missing_space_id}/occupancy"
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Space not found."