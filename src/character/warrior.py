from src.character.character import Character
from src.character.meleeHero import MeleeHero

class Warrior(MeleeHero):
    def __init__(self, name: str, max_health: int, base_damage: int, gold: int = 0):
        super().__init__(name, max_health, base_damage, gold)


    def attack(self, target: "Character"):
        damage = self.base_damage + (self.weapon.damage_stat if self.weapon else 0)
        damage = int(damage * 1.5)

        target.take_damage(damage)


