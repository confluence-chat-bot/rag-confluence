from pydantic_settings import BaseSettings, SettingsConfigDict

class ConfluenceProperties(BaseSettings):
    url: str = ""
    username: str = ""
    password: str = ""
    model_config = SettingsConfigDict(env_file=".env", env_prefix="CONFLUENCE_")
