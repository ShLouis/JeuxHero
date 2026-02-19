from character import Character
from character.manaBar import ManaBar
from inventory import Inventory


class Hero(Character):
    def __init__(self, name: str, max_health: int, base_damage: int, gold: int = 0):
        super().__init__(name, max_health, base_damage, gold)
        self.mana_bar = ManaBar(100)
        self.inventory = Inventory()
        self.weapon = None

    def attack(self, target: "Character"):
        if self.weapon is not None:
            target.take_damage(self.base_damage + self.weapon.damage_stat)
        else:
            target.take_damage(self.base_damage)

    def get_stats(self) -> dict:
        stats = super().get_stats()

        stats["weapon"] = {
            "name": self.weapon.name,
            "damage": self.weapon.damage_stat
        } if self.weapon else None
        stats["inventory_used_spaces"] = len(self.inventory.items)
        stats["inventory_size"] = self.inventory.spaces

        return stats
