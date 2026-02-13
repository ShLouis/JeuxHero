from abc import ABC, abstractmethod

from src.character.hero import Hero
from src.item.item import Item


class UsableItem(Item,ABC):
    def __init__(self, name: str, owner:"Hero"):
        super().__init__(name, owner)

    @abstractmethod
    def use(self):
        """Usable items implement this method"""
        pass
