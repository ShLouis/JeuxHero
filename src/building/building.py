from abc import ABC, abstractmethod
from character.hero import Hero


class Building(ABC):
    name:str
    description:str

    @abstractmethod
    def enter(self,hero:Hero):
        pass