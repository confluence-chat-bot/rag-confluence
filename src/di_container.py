from dependency_injector import containers, providers

from src.store.confluence.config.confluence_config import ConfluenceConfig
from src.store.confluence.config.confluence_properties import ConfluenceProperties


class DependencyContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    confluence_client = providers.Singleton(
        ConfluenceConfig,
        properties=ConfluenceProperties(),
    )
