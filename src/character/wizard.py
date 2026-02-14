import random

from src.character.magicHero import MagicHero


class Wizard(MagicHero):
    def __init__(self, name: str, max_health: int, base_damage: int, gold: int = 0):
        super().__init__(name, max_health, base_damage, gold)

    def take_damage(self, damage: int):
        if random.randint(1, 5) == 1:
            return
        super().take_damage(damage)

