from typing import Generic, TypeVar, Type

from sqlmodel import Session


ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):

    def __init__(self, model: Type[ModelType]):

        self.model = model