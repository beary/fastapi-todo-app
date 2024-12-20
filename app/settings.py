from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # postgres
    PG_USERNAME: str
    PG_PASSWORD: str
    PG_HOST: str
    PG_PORT: int
    PG_DBNAME: str

    # pyjwt
    JWT_SECRET: str

    # verification code expires
    CODE_EXP: int = 300

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()  # type: ignore
