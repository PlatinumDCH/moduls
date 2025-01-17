from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PG_URL: str = "postgresql+asyncpg://postgres:000000@localhost:5432/contacts"
    SECRET_KEY_JWT: str = "00000000000000000000000000000000"
    ALGORITHM: str = "HS256"
   
    model_config = SettingsConfigDict(
        extra="ignore"
        )
    
    class Confif:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()