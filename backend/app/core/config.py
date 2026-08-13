from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables.
    """

    # Base URL of the existing Payment API.
    payment_api_base_url: str

    