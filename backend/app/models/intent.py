from typing import Optional

from enum import Enum

from uuid import UUID

from app.models.user import User
from sqlmodel import Field, Relationship

from .base import BaseModel


class IntentType(str, Enum):

    NETWORKING = "Networking"

    FRIENDSHIP = "Friendship"

    CASUAL = "Casual Conversation"

    TRAVEL = "Travel Companion"


class Intent(BaseModel, table=True):

    user_id: UUID = Field(
        foreign_key="user.id",
        unique=True,
    )

    intent: IntentType

    user: Optional[User] = Relationship(back_populates="intent")
