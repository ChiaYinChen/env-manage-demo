from pydantic import BaseSettings


class Settings(BaseSettings):

    API_BASE: str
    DB_HOST: str
    DB_PORT: int
    DBCONN_STR: str
    DB_PASSWORD: str
    DB_NAME: str
    DEBUG: bool = False


class Testing(Settings):

    API_BASE = 'https://testing.example.com/api'
    DB_NAME = 'testing'
    DEBUG = True

    class Config:
        env_file = 'env/.test.env'


class Production(Settings):

    API_BASE = 'https://example.com/api'
    DB_NAME = 'production'

    class Config:
        env_file = 'env/.prod.env'


app_config = {
    'TESTING': Testing(),
    'PRODUCTION': Production(),
}
