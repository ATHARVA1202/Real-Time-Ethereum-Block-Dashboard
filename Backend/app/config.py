from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGODB_URI: str
    DB_NAME: str = "ethereum_db"
    COLLECTION_NAME: str = "ethereum"
    ALCHEMY_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
