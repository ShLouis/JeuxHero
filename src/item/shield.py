from src.character.hero import Hero
from src.item.equipableItem import EquipableItem

class Shield(EquipableItem):
    def __init__(self, name: str, owner: Hero, durability: int, defense_stat: int):
        super().__init__(name, owner, durability)
        self.defense_bonus = defense_stat
