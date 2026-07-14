from uuid import UUID

from pydantic import BaseModel

from app.models.intent import IntentType


class IntentCreate(BaseModel):
    """Payload for selecting a connection intent."""
    intent: IntentType


class IntentRead(BaseModel):
    """Public representation of a user's connection intent."""
    id: UUID
    user_id: UUID
    intent: IntentType


class IntentUpdate(BaseModel):
    """Payload for changing a user's connection intent."""
    intent: IntentType
