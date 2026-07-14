from uuid import UUID

from pydantic import BaseModel


class UserCreate(BaseModel):

    phone_number: str

    display_name: str

class UserRead(BaseModel):

    id: UUID

    phone_number: str

    display_name: str

    is_verified: bool

    is_active: bool

class UserUpdate(BaseModel):

    display_name: str | None = None