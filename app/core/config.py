from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    # Basic app settings
    app_name: str = os.getenv("APP_NAME")
    environment: str = os.getenv("ENVIRONMENT")
    version: str = os.getenv("VERSION")

    # CORS settings (JSON array format in .env)
    allowed_origins: list[str] = ["http://localhost:5173"]
    
    # Security settings (production, JSON array format in .env)
    allowed_hosts: list[str] = ["localhost"]

    # ML settings
    ml_models_path: str = os.getenv("ML_MODELS_PATH")

    # Logging settings
    log_level: str = os.getenv("LOG_LEVEL")
    log_format: str = "%(levelname)s - %(asctime)s - %(message)s"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

    @property
    def is_production(self) -> bool:
        return self.environment.lower() == "production"
    
    @property
    def is_development(self) -> bool:
        return self.environment.lower() == "development"

settings = Settings()