from pydantic_settings import BaseSettings,SettingsConfigDict
from functools import lru_cache
from pydantic import Field,PostgresDns


class Settings(BaseSettings):
    jwt_secret: str = Field(min_length=32)
    jwt_algorithm:str
    jwt_expire_minutes:int=30
    jwt_cookie_name :str = "access_token"
    jwt_cookie_samesite:str="lax"
    database_url:PostgresDns

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )
@lru_cache
def get_settings() -> Settings:
    return Settings()
