# Python 3.12+
from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "TrendFlow 2 - Gym Management"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = "sqlite:///./gym_flow.db"
    
    # Segurança (Exemplos)
    SECRET_KEY: str = "SUA_CHAVE_SUPER_SECRETA_DE_PRODUCAO"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    
    model_config = ConfigDict(case_sensitive=True)

settings = Settings()