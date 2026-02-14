from abc import ABC
from tarfile import HeaderError

from src.character.hero import Hero
from src.item.sword import Sword


class MeleeHero(Hero, ABC):
    def __init__(self, name: str, max_health: int, base_damage: int, gold: int = 0):
        super().__init__(name,max_health,base_damage,gold)


    def equip_sword(self,sword : "Sword"):
        self.weapon = sword
        sword.is_equipped = True

    def unequip_sword(self):
        self.weapon.is_equipped = False
        self.weapon = None

