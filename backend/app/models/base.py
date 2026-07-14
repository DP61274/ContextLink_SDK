from uuid import UUID, uuid4
from datetime import datetime

from sqlmodel import SQLModel, Field


class BaseModel(SQLModel):
    """Shared identifier and timestamp fields for persistent models."""
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        index=True
    )

    created_at: datetime = Field(
        default_factory=datetime.utcnow
    )

    updated_at: datetime = Field(
        default_factory=datetime.utcnow
    )
