from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class ProfileCreate(BaseModel):
    profession: Optional[str] = None
    bio: Optional[str] = None
    languages: Optional[str] = None
    interests: Optional[str] = None


class ProfileRead(BaseModel):
    id: UUID
    user_id: UUID
    profession: Optional[str]
    bio: Optional[str]
    languages: Optional[str]
    interests: Optional[str]


class ProfileUpdate(BaseModel):
    profession: Optional[str] = None
    bio: Optional[str] = None
    languages: Optional[str] = None
    interests: Optional[str] = None