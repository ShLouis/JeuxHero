from src.character.meleeHero import MeleeHero
from src.item.shield import Shield


class Paladin(MeleeHero):
    def __init__(self, name: str, max_health: int, base_damage: int, gold: int = 0):
        super().__init__(name, max_health, base_damage, gold)
        self.shield = None

    def equip_shied(self, shield: "Shield"):
        self.shield = shield
        shield.is_equipped = True

    def unequip_shied(self):
        self.shield.is_equipped = False
        self.shield = None

    def take_damage(self, damage: int):
        if self.shield is not None:
            damage_after_shield = max(damage - self.shield.defense_stat, 0)
            super().take_damage(damage_after_shield)
        else:
            super().take_damage(damage)
