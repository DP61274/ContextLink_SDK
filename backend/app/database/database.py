from sqlmodel import SQLModel, create_engine

# Import all implemented SQLModel tables before create_all() runs.
from app.models.intent import Intent
from app.models.trust_score import TrustScore
from app.models.user import User
from app.models.user_profile import UserProfile

from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    echo=True
)


def create_db():
    """Create database tables for every registered SQLModel entity."""
    SQLModel.metadata.create_all(engine)
