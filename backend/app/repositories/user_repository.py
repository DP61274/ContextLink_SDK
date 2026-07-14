from uuid import UUID
from datetime import datetime
from typing import Optional

from sqlmodel import Session, select

from app.models.user import User


class UserRepository:

    def create(
        self,
        session: Session,
        user: User
    ) -> User:

        session.add(user)

        session.commit()

        session.refresh(user)

        return user

    def get(
        self,
        session: Session,
        user_id: UUID
    ) -> Optional[User]:

        return session.get(User, user_id)

    def get_by_phone(
        self,
        session: Session,
        phone: str
    ) -> Optional[User]:

        statement = (
            select(User)
            .where(User.phone_number == phone)
        )

        return session.exec(statement).first()

    def update(self, session: Session, user: User) -> User:
        user.updated_at = datetime.utcnow()
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    def list(
        self,
        session: Session
    ) -> list[User]:

        return session.exec(
            select(User)
        ).all()
