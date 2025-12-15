from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class ConfluenceInterface(ABC):
    @abstractmethod
    def getAllDocuments(self) -> list[dict[str, Any]]:
        pass
