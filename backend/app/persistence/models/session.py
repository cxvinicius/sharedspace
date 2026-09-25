import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class SessionModel(Base):
    __tablename__ = "sessions"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    space_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("spaces.id"),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    started_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    confirmation_requested_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    ended_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )