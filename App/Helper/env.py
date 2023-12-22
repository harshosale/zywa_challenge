from pydantic import BaseSettings


class EnvironmentVariables(BaseSettings):
    ZYWA_ENV: str
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    SUPER_ADMIN_MOBILE_NUMBER: str
    TOKEN_EXPIRE_AFTER_MINS: int
    SECRET_KEY: str
    ALGORITHM: str

    class Config:
        env_file = "../.env"


envVars = EnvironmentVariables()
