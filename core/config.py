from typing import Any, Dict, Optional
from pydantic import BaseSettings, PostgresDsn, validator

class Settings(BaseSettings):
    api_v1: str = "/api/v1"
    database_hostname: str
    database_password: str
    database_name: str
    database_username: str

    DATABASE_URI: Optional[PostgresDsn] = None

    @validator("DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]):
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("database_username"),
            password=values.get("database_password"),
            host=values.get("database_hostname"),
            path=f"/{values.get('database_name') or ''}",
        )

    class Config:
        env_file = '.env'

settings = Settings()