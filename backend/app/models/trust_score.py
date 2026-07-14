from uuid import UUID
from typing import Optional

from sqlmodel import Field, Relationship

from app.models.user import User

from .base import BaseModel


class TrustScore(BaseModel, table=True):

    user_id: UUID = Field(
        foreign_key="user.id",
        unique=True,
    )

    score: int = 50

    reports: int = 0

    verified_phone: bool = False

    profile_completed: bool = False

    user: Optional[User] = Relationship(back_populates="trust_score")
