from typing import Optional

from uuid import UUID

from app.models.user import User
from sqlmodel import Field, Relationship

from .base import BaseModel


class UserProfile(BaseModel, table=True):

    user_id: UUID = Field(
        foreign_key="user.id",
        unique=True
    )

    profession: Optional[str] = None

    bio: Optional[str] = None

    languages: Optional[str] = None

    interests: Optional[str] = None

    user: Optional[User] = Relationship(back_populates="profile")
