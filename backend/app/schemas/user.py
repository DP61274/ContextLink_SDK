from uuid import UUID

from pydantic import BaseModel


class UserCreate(BaseModel):
    """Payload for creating a user."""

    phone_number: str

    display_name: str


class UserRead(BaseModel):
    """Public representation of a user."""

    id: UUID

    phone_number: str

    display_name: str

    is_verified: bool

    is_active: bool


class UserUpdate(BaseModel):
    """Payload for updating editable user details."""

    display_name: str | None = None
