from Helper.env import envVars
from peewee import PostgresqlDatabase

PostgresDB = {
    "dev": PostgresqlDatabase(
        envVars.DATABASE_NAME,
        user=envVars.DATABASE_USER,
        password=envVars.DATABASE_PASSWORD,
        host=envVars.DATABASE_HOST,
        port=envVars.DATABASE_PORT,
        autorollback=True,
    ),
    "test": PostgresqlDatabase(
        (envVars.DATABASE_NAME + "_test"),
        user=envVars.DATABASE_USER,
        password=envVars.DATABASE_PASSWORD,
        host=(envVars.DATABASE_HOST),
        port=(envVars.DATABASE_PORT - 1111),
        autorollback=True,
    ),
}
database = PostgresDB[envVars.ZYWA_ENV]
