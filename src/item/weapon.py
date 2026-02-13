from equipableItem import EquipableItem
from src.character.hero import Hero

class Weapon(EquipableItem):
    def __init__(self, name: str, owner: Hero, durability: int, damage_stat: int):
        super().__init__(name, owner, durability)
        self.damage_stat = damage_stat
