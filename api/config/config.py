from dotenv import load_dotenv
import os

from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    TITLE: str = os.getenv('TITLE')
    VERSION: str = '1.0.0'
    DESCRIPTION: str = os.getenv('DESCRIPTION')
    OPENAPI_PREFIX: str = os.getenv('OPENAPI_PREFIX')
    DOCS_URL: str = '/docs'
    REDOC_URL: str = '/redoc'
    OPENAPI_URL: str = '/openapi.json'
    API_PREFIX: str = '/api'
    DB_ECHO_LOG: bool = True if os.getenv('DEBUG') == 'True' else False

    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_DB: str = os.getenv('POSTGRES_DB')
    POSTGRES_API_DB: str = os.getenv('POSTGRES_API_DB')
    POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER')
    POSTGRES_PORT: str = os.getenv('POSTGRES_PORT')

    @property
    def sync_database_url(self) -> str:
        return (
            f'postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}'
            f'@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_API_DB}'
        )

    @property
    def async_database_url(self) -> str:
        return (
            f'postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}'
            f'@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_API_DB}'
        )


settings = Settings()
