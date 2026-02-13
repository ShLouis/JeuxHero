from abc import ABC
from healthBar import HealthBar
from wallet import Wallet


class Character(ABC):
    def __init__(self, name: str, max_health: int, base_damage: int, gold: int = 0):
        self.name = name
        self.health_bar = HealthBar(max_health)
        self.base_damage = base_damage
        self.wallet = Wallet(gold)

    def is_alive(self) -> bool:
        return not self.health_bar.is_empty()

    def attack(self, target: "Character"):
        target.take_damage(self.base_damage)

    def take_damage(self, amount: int):
        self.health_bar.lose_health(amount)



