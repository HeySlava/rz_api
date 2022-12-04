from pydantic import BaseSettings


class Settings(BaseSettings):
    port: int = 8080
    host: str = '0.0.0.0'
    debug: bool = False
    conn_str: str = 'sqlite:///:memory:'

    class Config:
        env_prefix = 'rz_'


settings = Settings(
        conn_str='sqlite:///rz.sqlite',
        _env_file='.env',
        _env_file_encoding='utf-8'
    )
