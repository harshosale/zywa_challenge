from pydantic import BaseSettings


class EnvironmentVariables(BaseSettings):
    ZYWA_ENV: str
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int

    class Config:
        env_file = "../.env"


envVars = EnvironmentVariables()
