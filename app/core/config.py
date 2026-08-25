"""
Configurations centralizadas da aplicação TrendFlow 2
"""
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configurações gerais da aplicação"""
    
    # Projeto
    PROJECT_NAME: str = "TrendFlow 2 - Gym Management System"
    API_V1_STR: str = "/api/v1"
    VERSION: str = "2.0.0"
    
    # Banco de dados
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/trendflow2"
    SQLALCHEMY_ECHO: bool = False
    
    # Segurança
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # CORS
    ALLOWED_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
    ]
    
    # Rate Limiting
    RATE_LIMIT_ENABLED: bool = True
    RATE_LIMIT_REQUESTS: int = 100
    RATE_LIMIT_PERIOD: int = 60  # segundos
    
    # Pagamentos (mock/simulação)
    PAYMENT_GATEWAY_MOCK_MODE: bool = True
    PAYMENT_WEBHOOK_SECRET: str = "webhook-secret"
    
    # Email (preparado para integração)
    SMTP_ENABLED: bool = False
    SMTP_HOST: Optional[str] = None
    SMTP_PORT: int = 587
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    
    # WhatsApp/SMS (preparado para integração)
    MESSAGING_ENABLED: bool = False
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
