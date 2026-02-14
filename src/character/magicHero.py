from abc import ABC
from tarfile import HeaderError

from src.character.hero import Hero
from src.item.staff import Staff


class MagicHero(Hero, ABC):
    def __init__(self, name: str, max_health: int, base_damage: int, gold: int = 0):
        super().__init__(name,max_health,base_damage,gold)


    def equip_staff(self,staff : "Staff"):
        self.weapon = staff
        staff.is_equipped = True

    def unequip_staff(self):
        self.weapon.is_equipped = False
        self.weapon = None

