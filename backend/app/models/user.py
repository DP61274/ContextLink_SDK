from typing import Optional

from sqlmodel import Field, Relationship

from .base import BaseModel


class User(BaseModel, table=True):

    phone_number: str = Field(index=True, unique=True)

    display_name: str

    is_active: bool = True

    is_verified: bool = False

    profile: Optional["UserProfile"] = Relationship(back_populates="user")

    intent: Optional["Intent"] = Relationship(back_populates="user")

    trust_score: Optional["TrustScore"] = Relationship(back_populates="user")
