from sqlmodel import SQLModel, create_engine

from app.core.config import settings

# Add this temporary print line right here:
print(f"--- DEBUG: DATABASE_URL is: '{settings.DATABASE_URL}' ---")

engine = create_engine(
    settings.DATABASE_URL,
    echo=True
)


def create_db():
    SQLModel.metadata.create_all(engine)