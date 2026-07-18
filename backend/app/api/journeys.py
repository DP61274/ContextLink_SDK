"""HTTP routes for shared-context journeys."""

from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.database.session import get_session
from app.schemas.journey import (
    JourneyCreate,
    JourneyJoin,
    JourneyParticipantRead,
    JourneyRead,
)
from app.services.journey_service import JourneyService

router = APIRouter(prefix="/journeys", tags=["Journeys"])
journey_service = JourneyService()


@router.post("/", response_model=JourneyRead, status_code=status.HTTP_201_CREATED)
def create_journey(journey_in: JourneyCreate, session: Session = Depends(get_session)):
    return journey_service.create_journey(session, journey_in)


@router.get("/", response_model=list[JourneyRead])
def list_active_journeys(session: Session = Depends(get_session)):
    return journey_service.list_active_journeys(session)


@router.get("/{journey_id}", response_model=JourneyRead)
def get_journey(journey_id: UUID, session: Session = Depends(get_session)):
    return journey_service.get_journey(session, journey_id)


@router.post(
    "/{journey_id}/join",
    response_model=JourneyParticipantRead,
    status_code=status.HTTP_201_CREATED,
)
def join_journey(
    journey_id: UUID,
    participant_in: JourneyJoin,
    session: Session = Depends(get_session),
):
    return journey_service.join_journey(session, journey_id, participant_in)


@router.post("/{journey_id}/leave", response_model=JourneyParticipantRead)
def leave_journey(
    journey_id: UUID, user_id: UUID, session: Session = Depends(get_session)
):
    return journey_service.leave_journey(session, journey_id, user_id)


@router.patch("/{journey_id}/end", response_model=JourneyRead)
def end_journey(journey_id: UUID, session: Session = Depends(get_session)):
    return journey_service.end_journey(session, journey_id)
