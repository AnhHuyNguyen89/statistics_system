from abc import ABC, abstractmethod


class AbstractFile(ABC):
    """Abstract base class. Can not be instantiated"""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def _open(self):
        pass
