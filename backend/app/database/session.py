from collections.abc import Generator

from sqlmodel import Session

from app.database.database import engine


def get_session() -> Generator[Session, None, None]:
    """Yield a database session and close it after the request."""
    with Session(engine) as session:
        yield session
