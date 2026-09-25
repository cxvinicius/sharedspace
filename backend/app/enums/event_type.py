from enum import Enum


class EventType(str, Enum):
    CHECK_IN = "CHECK_IN"
    CHECK_OUT = "CHECK_OUT"
    RENEWAL = "RENEWAL"
    AUTO_TERMINATION = "AUTO_TERMINATION"