from pydantic import BaseSettings


class Settings(BaseSettings):
    port: int = 8080
    host: str = '0.0.0.0'

    class Config:
        env_prefix = 'rz_'


settings = Settings(
        _env_file='.env',
        _env_file_encoding='utf-8'
    )
