from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    #django app
    API_PORT: int


    #postgres
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int


    #telegram bot
    BOT_TOKEN: str
    BOT_URL: str


    model_config = SettingsConfigDict(env_file=".env", extra="allow")
