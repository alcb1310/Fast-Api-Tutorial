import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'

load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER')
    # default postgres port is 5432
    POSTGRES_PORT: str = os.getenv('POSTGRES_PORT', 5432)
    POSTGRES_DB: str = os.getenv('POSTGRES_DB', 'tdd')
    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    # os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 2
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    ALGORITHM: str = os.getenv('ALGORITHM')


settings = Settings()
