from uuid import UUID

from pydantic import BaseModel

from app.models.intent import IntentType


class IntentCreate(BaseModel):
    intent: IntentType


class IntentRead(BaseModel):
    id: UUID
    user_id: UUID
    intent: IntentType


class IntentUpdate(BaseModel):
    intent: IntentType