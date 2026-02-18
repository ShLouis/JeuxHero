from character.magicHero import MagicHero
from src.character.character import Character
from src.character.meleeHero import MeleeHero

class Undead(MeleeHero,MagicHero):
    def __init__(self, name: str, max_health: int, base_damage: int, gold: int = 0):
        super().__init__(name, max_health, base_damage, gold)
        self.immortal = True


    def attack(self, target: "Character"):
        damage = self.base_damage + (self.weapon.damage_stat if self.weapon else 0)
        damage = int(damage * 0.8)

        target.take_damage(damage)

    def take_damage(self, damage: int):
        super().take_damage(damage)
        if self.immortal and self.health_bar.health <= 0:
            self.health_bar.health = 100
            self.immortal = False