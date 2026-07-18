"""Database access operations for journeys and their participants."""

from datetime import datetime
from uuid import UUID

from sqlmodel import Session, select

from app.models.journey import Journey, JourneyStatus
from app.models.journey_participant import JourneyParticipant


class JourneyRepository:
    """Persist and query shared context journeys."""

    def create(self, session: Session, journey: Journey) -> Journey:
        session.add(journey)
        session.commit()
        session.refresh(journey)
        return journey

    def get(self, session: Session, journey_id: UUID) -> Journey | None:
        return session.get(Journey, journey_id)

    def update(self, session: Session, journey: Journey) -> Journey:
        journey.updated_at = datetime.utcnow()
        session.add(journey)
        session.commit()
        session.refresh(journey)
        return journey

    def list_active(self, session: Session) -> list[Journey]:
        statement = select(Journey).where(Journey.status == JourneyStatus.ACTIVE)
        return list(session.exec(statement).all())

    def find_by_route(self, session: Session, route_hash: str) -> list[Journey]:
        statement = select(Journey).where(
            Journey.route_hash == route_hash,
            Journey.status == JourneyStatus.ACTIVE,
        )
        return list(session.exec(statement).all())

    def create_participant(
        self, session: Session, participant: JourneyParticipant
    ) -> JourneyParticipant:
        session.add(participant)
        session.commit()
        session.refresh(participant)
        return participant

    def get_active_participant(
        self, session: Session, journey_id: UUID, user_id: UUID
    ) -> JourneyParticipant | None:
        statement = select(JourneyParticipant).where(
            JourneyParticipant.journey_id == journey_id,
            JourneyParticipant.user_id == user_id,
            JourneyParticipant.left_at.is_(None),
        )
        return session.exec(statement).first()

    def count_active_participants(self, session: Session, journey_id: UUID) -> int:
        statement = select(JourneyParticipant).where(
            JourneyParticipant.journey_id == journey_id,
            JourneyParticipant.left_at.is_(None),
        )
        return len(session.exec(statement).all())

    def leave_participant(
        self, session: Session, participant: JourneyParticipant
    ) -> JourneyParticipant:
        participant.left_at = datetime.utcnow()
        participant.updated_at = datetime.utcnow()
        session.add(participant)
        session.commit()
        session.refresh(participant)
        return participant
