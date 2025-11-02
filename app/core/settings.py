from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str = "change-me"
    JWT_ALG: str = "HS256"
    JWT_EXPIRE_MIN: int = 60 * 24

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
