from character import Character
from inventory import Inventory

class Hero(Character):
    def __init__(self, name: str, max_health: int, base_damage: int, gold: int = 0):
        super().__init__(name, max_health, base_damage, gold)
        self.inventory = Inventory()
        self.weapon = None
