from abc import ABC

from src.item.item import Item
from src.character.hero import Hero


class EquipableItem(Item, ABC):
    def __init__(self, name: str, owner: Hero, durability: int):
        super().__init__(name, owner)
        self.durability = durability
        self.is_equipped = False

    def reduce_durability(self):
        self.durability -= 1
        if self.durability <= 0:
            self.break_item()

    def break_item(self):
        """Handles item breaking"""
        self.is_equipped = False
        self.owner.weapon = None
        self.owner = None
