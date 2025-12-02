from atlassian import Confluence
import requests
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class ConfluenceConfig(BaseSettings):
    url: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None

    model_config = SettingsConfigDict(env_file=".env", env_prefix="CONFLUENCE_")

    def __init__(self, url: str = None, username: str = None, password: str = None, **kwargs):
        super().__init__(url=url, username=username, password=password, **kwargs)
        
        self.session = requests.Session()
        self.confluence = Confluence(
            url=self.url,
            username=self.username,
            password=self.password,
            session=self.session,
        )

    def get_session(self):
        return self.confluence
