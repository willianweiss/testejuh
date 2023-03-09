from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_NAME: str
    POSTGRES_URL: str
    SECRET_KEY: str
    JWT_ALGORITHM: str

    class Config:
        env_file = ".env"


settings = Settings()
