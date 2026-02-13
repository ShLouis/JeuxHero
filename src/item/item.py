from abc import ABC
from src.character.hero import Hero

class Item(ABC):
    def __init__(self, name: str, owner:"Hero"):
        self.name = name
        self.owner = owner

