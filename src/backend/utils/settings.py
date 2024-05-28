from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    log_level: str = Field(alias="LOG_LEVEL", default="INFO")

    postgres_db: str = Field(alias="POSTGRES_DB", default="postgres")
    postgres_user: str = Field(alias="POSTGRES_USER", default="postgres")
    postgres_password: str = Field(alias="POSTGRES_PASSWORD", default="postgres")
    postgres_host: str = Field(alias="POSTGRES_HOST", default="localhost")
    postgres_port: str = Field(alias="POSTGRES_PORT", default="5432")

    redis_db: int = Field(alias="REDIS_DB",default=0)
    redis_host: str = Field(alias="REDIS_HOST", default="localhost")
    redis_port: int = Field(alias="REDIS_PORT",default=6379)

    access_token_expire_minutes: int = Field(alias="ACCESS_TOKEN_EXPIRE_MINUTES", default=120)
    secret_key: str = Field(alias="SECRET_KEY", default="simple")
    algorithm: str = Field(alias="ALGORITHM", default="")

    @property
    def get_db_url(self) -> str:
        return f"postgresql+psycopg://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}"
    @property
    def get_redis_url(self) -> str:
        return f"redis://{self.redis_host}:{self.redis_port}/{self.redis_db}"
    class Config:
        env_file = ".env"


settings = Settings()
