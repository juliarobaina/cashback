from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_TYPE: str
    DB_DRIVER: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    model_config = SettingsConfigDict(env_file=".env")


db_settings = Settings()