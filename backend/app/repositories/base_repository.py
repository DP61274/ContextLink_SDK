from typing import Generic, TypeVar, Type

from sqlmodel import Session


ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    """Base class for repositories bound to a SQLModel type."""

    def __init__(self, model: Type[ModelType]):
        """Store the model handled by this repository."""
        self.model = model
