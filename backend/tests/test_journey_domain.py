"""Journey-domain service tests using an isolated SQLite database."""

import unittest

from fastapi import HTTPException
from sqlmodel import SQLModel, Session, create_engine

from app.models.intent import Intent
from app.models.journey import JourneyStatus
from app.models.journey_participant import JourneyParticipant
from app.models.trust_score import TrustScore
from app.models.user import User
from app.models.user_profile import UserProfile
from app.schemas.journey import JourneyCreate, JourneyJoin
from app.services.journey_service import JourneyService
from app.utils.hashing import generate_route_hash


class JourneyDomainTests(unittest.TestCase):
    def setUp(self) -> None:
        self.engine = create_engine("sqlite://")
        SQLModel.metadata.create_all(self.engine)
        self.service = JourneyService()

    def test_journey_lifecycle_and_capacity(self) -> None:
        with Session(self.engine) as session:
            user = User(phone_number="+254700000001", display_name="Amina")
            session.add(user)
            session.commit()
            session.refresh(user)

            journey = self.service.create_journey(
                session,
                JourneyCreate(
                    origin="Nairobi CBD",
                    destination="Westlands",
                    context_type="Traffic",
                    host_application="Demo Host",
                    max_participants=1,
                ),
            )
            self.assertEqual(
                journey.route_hash, generate_route_hash("Nairobi CBD", "Westlands")
            )

            participant = self.service.join_journey(
                session,
                journey.id,
                JourneyJoin(user_id=user.id, intent="Networking", opted_in=True),
            )
            self.assertTrue(participant.opted_in)
            self.assertIsNotNone(self.service.leave_journey(session, journey.id, user.id).left_at)

            ended = self.service.end_journey(session, journey.id)
            self.assertEqual(ended.status, JourneyStatus.ENDED)
            with self.assertRaises(HTTPException):
                self.service.join_journey(
                    session, journey.id, JourneyJoin(user_id=user.id, intent="Networking")
                )


if __name__ == "__main__":
    unittest.main()
