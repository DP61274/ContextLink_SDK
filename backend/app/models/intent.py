from typing import Optional

from enum import Enum

from uuid import UUID

from app.models.user import User
from sqlmodel import Field, Relationship

from .base import BaseModel


class IntentType(str, Enum):
    """Social connection intents a user may select."""

    NETWORKING = "Networking"

    FRIENDSHIP = "Friendship"

    CASUAL = "Casual Conversation"

    TRAVEL = "Travel Companion"


class Intent(BaseModel, table=True):
    """The current connection intent selected by a user."""

    user_id: UUID = Field(
        foreign_key="user.id",
        unique=True,
    )

    intent: IntentType

    user: Optional[User] = Relationship(back_populates="intent")
