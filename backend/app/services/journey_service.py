"""Business operations for the privacy-first journey domain."""

from datetime import datetime
from uuid import UUID

from fastapi import HTTPException
from sqlmodel import Session

from app.models.journey import Journey, JourneyStatus
from app.models.journey_participant import JourneyParticipant
from app.repositories.journey_repository import JourneyRepository
from app.repositories.user_repository import UserRepository
from app.schemas.journey import JourneyCreate, JourneyJoin
from app.utils.hashing import generate_route_hash


class JourneyService:
    """Coordinate journey lifecycle and participant consent rules."""

    def __init__(self) -> None:
        self.repository = JourneyRepository()
        self.user_repository = UserRepository()

    def create_journey(self, session: Session, journey_in: JourneyCreate) -> Journey:
        """Create a context and derive its opaque route identifier internally."""
        journey = Journey(
            **journey_in.model_dump(),
            route_hash=generate_route_hash(journey_in.origin, journey_in.destination),
        )
        return self.repository.create(session, journey)

    def get_journey(self, session: Session, journey_id: UUID) -> Journey:
        journey = self.repository.get(session, journey_id)
        if not journey:
            raise HTTPException(status_code=404, detail="Journey not found")
        return journey

    def list_active_journeys(self, session: Session) -> list[Journey]:
        return self.repository.list_active(session)

    def join_journey(
        self, session: Session, journey_id: UUID, participant_in: JourneyJoin
    ) -> JourneyParticipant:
        """Join an active journey once, respecting capacity and account state."""
        journey = self.get_journey(session, journey_id)
        if journey.status != JourneyStatus.ACTIVE:
            raise HTTPException(status_code=400, detail="Only active journeys can be joined")

        user = self.user_repository.get(session, participant_in.user_id)
        if not user or not user.is_active:
            raise HTTPException(status_code=404, detail="Active user not found")

        if self.repository.get_active_participant(session, journey_id, user.id):
            raise HTTPException(status_code=400, detail="User is already in this journey")

        if self.repository.count_active_participants(session, journey_id) >= journey.max_participants:
            raise HTTPException(status_code=400, detail="Journey has reached its participant limit")

        participant = JourneyParticipant(
            journey_id=journey.id,
            **participant_in.model_dump(),
        )
        return self.repository.create_participant(session, participant)

    def leave_journey(
        self, session: Session, journey_id: UUID, user_id: UUID
    ) -> JourneyParticipant:
        """Record a participant's departure without deleting their history."""
        self.get_journey(session, journey_id)
        participant = self.repository.get_active_participant(session, journey_id, user_id)
        if not participant:
            raise HTTPException(status_code=404, detail="Active journey participation not found")
        return self.repository.leave_participant(session, participant)

    def end_journey(self, session: Session, journey_id: UUID) -> Journey:
        """End a journey and prevent new joins while preserving its history."""
        journey = self.get_journey(session, journey_id)
        if journey.status == JourneyStatus.CANCELLED:
            raise HTTPException(status_code=400, detail="Cancelled journeys cannot be ended")
        if journey.status == JourneyStatus.ENDED:
            return journey
        journey.status = JourneyStatus.ENDED
        journey.ended_at = datetime.utcnow()
        return self.repository.update(session, journey)
