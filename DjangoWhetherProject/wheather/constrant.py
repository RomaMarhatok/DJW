from pydantic import BaseSettings


class WheatherApiConstant(BaseSettings):
    WHEATHER_API_KEY: str
    BASE_WHEATHER_API_URL: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
