from src.item.potion import Potion
from src.character.hero import Hero

class HealthPotion(Potion):
    def __init__(self, owner: Hero, heal_amount: int):
        super().__init__("Health Potion", owner)
        self.heal_amount = heal_amount

    def apply_effects(self, hero: Hero):
        """Heal the hero by the potion’s heal_amount."""
        if hero.is_alive():
            hero.health_bar.heal(self.heal_amount)

