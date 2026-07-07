from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "ClassVision"
    DATABASE_URL: str = "sqlite:///./classvision.db"
    OLLAMA_HOST: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "qwen3:4b"

    class Config:
        env_file = ".env"


settings = Settings()
