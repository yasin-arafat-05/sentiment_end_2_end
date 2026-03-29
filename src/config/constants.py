from pydantic import SecretStr
from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    
    # ====== 1.mlflow and dagshub ======
    MLFLOW_DAGSHUB_TRACKING_URI : str 
    DAGSHUB_REPO_OWNER:str 
    DAGSHUB_REPO_NAME:str 
    
    
    model_config = SettingsConfigDict(
        env_file=".env"
    )
    
CONFIG = Settings()

