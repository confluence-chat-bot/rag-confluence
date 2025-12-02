from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class DataProcessingInterface(ABC):
    
    @abstractmethod
    def process(self):
        pass
    

