from datetime import datetime
from enum import Enum
from typing import Optional

from sqlmodel import Field, Relationship

from .base import BaseModel


class ContextType(str, Enum):
    TRAFFIC = "Traffic"
    BUS = "Bus"
    TRAIN = "Train"
    AIRPORT = "Airport"
    EVENT = "Event"
    CAMPUS = "Campus"
    CONFERENCE = "Conference"


class JourneyStatus(str, Enum):
    ACTIVE = "Active"
    ENDED = "Ended"
    CANCELLED = "Cancelled"


class Journey(BaseModel, table=True):
    """
    Represents a shared context that users may join.
    """

    origin: str

    destination: str

    host_application: str

    route_hash: str = Field(index=True)

    context_type: ContextType

    status: JourneyStatus = JourneyStatus.ACTIVE

    max_participants: int = Field(default=20, ge=1)

    started_at: datetime = Field(default_factory=datetime.utcnow)

    ended_at: Optional[datetime] = None

    participants: list["JourneyParticipant"] = Relationship(
        back_populates="journey"
    )
