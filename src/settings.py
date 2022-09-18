from pydantic import BaseSettings


class Settings(BaseSettings):
    """Класс для настроек прилоложения"""
    server_host: str = '127.0.0.1'
    server_port: int = 8000


settings = Settings()
