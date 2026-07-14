from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""
    PROJECT_NAME: str = "ContextLink SDK"

    API_VERSION: str = "v1"

    DATABASE_URL: str

    OPENAI_API_KEY: str = ""

    AFRICAS_TALKING_USERNAME: str = ""

    AFRICAS_TALKING_API_KEY: str = ""

    SECRET_KEY: str

    class Config:
        """Configure Pydantic settings sources."""
        env_file = ".env"


settings = Settings()
