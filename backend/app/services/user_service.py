from uuid import UUID
from fastapi import HTTPException, status
from sqlmodel import Session

from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.models.user import User

class UserService:
    def __init__(self):
        # Instance-level attribute protects state isolation
        self.repository = UserRepository()

    def create_user(self, session: Session, user_in: UserCreate) -> User:
        # Check if the user already exists by phone number
        existing_user = self.repository.get_by_phone(session, phone=user_in.phone_number)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A user with this phone number already exists."
            )
        
        db_user = User(
            phone_number=user_in.phone_number,
            display_name=user_in.display_name
        )
        return self.repository.create(session, db_user)

    def verify_user(self, session: Session, user_id: UUID) -> User:
        user = self.repository.get(session, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        user.is_verified = True
        return self.repository.update(session, user) # Safely returns the database object

    def deactivate_user(self, session: Session, user_id: UUID) -> User:
        user = self.repository.get(session, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        user.is_active = False
        return self.repository.update(session, user) # Safely returns the database object
