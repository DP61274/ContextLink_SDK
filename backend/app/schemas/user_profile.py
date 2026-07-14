from uuid import UUID
from pydantic import BaseModel


class ProfileCreate(BaseModel):
    """Payload for creating a user profile."""

    profession: str | None = None
    bio: str | None = None
    languages: str | None = None
    interests: str | None = None


class ProfileRead(BaseModel):
    """Public representation of a user profile."""
    id: UUID
    user_id: UUID
    profession: str | None
    bio: str | None
    languages: str | None
    interests: str | None


class ProfileUpdate(BaseModel):
    """Payload for updating a user profile."""

    profession: str | None = None
    bio: str | None = None
    languages: str | None = None
    interests: str | None = None
