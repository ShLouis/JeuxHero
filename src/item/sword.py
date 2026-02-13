from src.character.hero import Hero
from src.item.weapon import Weapon


class Sword(Weapon):
    def __init__(self, name: str, owner: Hero, durability: int, damage_bonus: int):
        super().__init__(name, owner, durability, damage_bonus)
