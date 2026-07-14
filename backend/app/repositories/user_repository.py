from uuid import UUID
from datetime import datetime
from typing import Optional

from sqlmodel import Session, select

from app.models.user import User


class UserRepository:
    """Database access operations for users."""

    def create(
        self,
        session: Session,
        user: User
    ) -> User:
        """Persist a new user and return its refreshed record."""
        session.add(user)

        session.commit()

        session.refresh(user)

        return user

    def get(
        self,
        session: Session,
        user_id: UUID
    ) -> Optional[User]:
        """Return a user by ID, if it exists."""
        return session.get(User, user_id)

    def get_by_phone(
        self,
        session: Session,
        phone: str
    ) -> Optional[User]:
        """Return a user by phone number, if it exists."""
        statement = (
            select(User)
            .where(User.phone_number == phone)
        )

        return session.exec(statement).first()

    def update(self, session: Session, user: User) -> User:
        """Persist changes to an existing user."""
        user.updated_at = datetime.utcnow()
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    def list(
        self,
        session: Session
    ) -> list[User]:
        """Return all users."""
        return session.exec(
            select(User)
        ).all()
