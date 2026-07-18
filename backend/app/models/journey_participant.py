from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID

from sqlmodel import Field, Relationship

from app.models.intent import IntentType
from app.models.journey import Journey
from app.models.user import User

from .base import BaseModel


class ParticipantRole(str, Enum):
    """A participant's role within a shared context."""

    PARTICIPANT = "Participant"
    HOST = "Host"


class ParticipantVisibility(str, Enum):
    """Controls whether a participant can be considered for matching."""

    VISIBLE = "Visible"
    HIDDEN = "Hidden"


class JourneyParticipant(BaseModel, table=True):
    """A user's opt-in participation in a journey context."""

    journey_id: UUID = Field(foreign_key="journey.id", index=True)
    user_id: UUID = Field(foreign_key="user.id", index=True)
    seat_type: Optional[str] = None
    role: ParticipantRole = ParticipantRole.PARTICIPANT
    joined_at: datetime = Field(default_factory=datetime.utcnow)
    left_at: Optional[datetime] = None
    intent: IntentType
    visibility: ParticipantVisibility = ParticipantVisibility.VISIBLE
    opted_in: bool = False

    journey: Journey = Relationship(back_populates="participants")
    user: User = Relationship(back_populates="journey_participations")
