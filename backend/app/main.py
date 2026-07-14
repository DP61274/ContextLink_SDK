from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.users import router as users_router
from app.core.config import settings
from app.database.database import create_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
    lifespan=lifespan,
)
app.include_router(users_router)

# @app.on_event("startup")
# def startup():
#    create_db()

@app.get("/")
def root():
    return {"message": "Welcome to ContextLink SDK"}


@app.get("/health")
def health():
    return {"status": "healthy"}