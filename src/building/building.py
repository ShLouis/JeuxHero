from abc import ABC, abstractmethod
from src.character.hero import Hero


class Building(ABC):
    name: str
    description: str

    @abstractmethod
    def enter(self, hero: Hero):
        pass
