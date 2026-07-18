from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.journeys import router as journeys_router
from app.api.users import router as users_router
from app.core.config import settings
from app.database.database import create_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Create database tables when the application starts."""
    create_db()
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
    lifespan=lifespan,
)
app.include_router(users_router)
app.include_router(journeys_router)


@app.get("/")
def root():
    """Return a welcome message for the API root."""
    return {"message": "Welcome to ContextLink SDK"}


@app.get("/health")
def health():
    """Report whether the API process is available."""
    return {"status": "healthy"}
