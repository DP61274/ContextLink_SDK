from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field

from app.models.journey import ContextType, JourneyStatus
from app.models.intent import IntentType
from app.models.journey_participant import ParticipantRole, ParticipantVisibility


class JourneyCreate(BaseModel):
    origin: str
    destination: str
    context_type: ContextType
    host_application: str
    max_participants: int = Field(default=20, ge=1)


class JourneyRead(BaseModel):
    id: UUID
    origin: str
    destination: str
    host_application: str
    route_hash: str
    context_type: ContextType
    status: JourneyStatus
    max_participants: int
    started_at: datetime
    ended_at: Optional[datetime]


class JourneyUpdate(BaseModel):
    status: Optional[JourneyStatus] = None
    ended_at: Optional[datetime] = None


class JourneyJoin(BaseModel):
    """A user's preferences for one particular context."""

    user_id: UUID
    intent: IntentType
    seat_type: Optional[str] = None
    role: ParticipantRole = ParticipantRole.PARTICIPANT
    visibility: ParticipantVisibility = ParticipantVisibility.VISIBLE
    opted_in: bool = False


class JourneyParticipantRead(BaseModel):
    """Safe representation of a participant's journey settings."""

    id: UUID
    journey_id: UUID
    user_id: UUID
    seat_type: Optional[str]
    role: ParticipantRole
    joined_at: datetime
    left_at: Optional[datetime]
    intent: IntentType
    visibility: ParticipantVisibility
    opted_in: bool
