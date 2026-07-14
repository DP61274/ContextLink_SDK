from uuid import UUID
from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.database.session import get_session
from app.schemas.user import UserCreate, UserRead
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])
user_service = UserService()


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register_user(user_in: UserCreate, session: Session = Depends(get_session)):
    """Register a new ContextLink user."""
    return user_service.create_user(session, user_in)


@router.patch("/{user_id}/verify", response_model=UserRead)
def verify_user(user_id: UUID, session: Session = Depends(get_session)):
    """Mark a user as verified."""
    return user_service.verify_user(session, user_id)


@router.patch("/{user_id}/deactivate", response_model=UserRead)
def deactivate_user(user_id: UUID, session: Session = Depends(get_session)):
    """Deactivate a user without deleting their record."""
    return user_service.deactivate_user(session, user_id)
