from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGODB_URI: str
    DB_NAME: str = "<YOUR_DB_NAME>"
    COLLECTION_NAME: str = "<YOUR_COLLECTION_NAME>"
    ALCHEMY_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
