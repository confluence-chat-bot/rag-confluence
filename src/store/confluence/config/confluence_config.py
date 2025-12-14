from atlassian import Confluence
import requests

from src.store.confluence.config.confluence_properties import ConfluenceProperties


class ConfluenceConfig:
    def __init__(self, properties:ConfluenceProperties) -> None:
        session: requests.Session = requests.Session()

        self._confluence: Confluence = Confluence(
            url=properties.url,
            username=properties.username,
            password=properties.password,
            session=session,
        )

    def get_session(self) -> Confluence:
        return self._confluence
