from src.item.potion import Potion
from src.character.hero import Hero

class ManaPotion(Potion):
    def __init__(self, owner: Hero, mana_amount: int):
        super().__init__("Mana Potion", owner)
        self.mana_amount = mana_amount

    def apply_effects(self, hero: Hero):
        """Restore the mana of the hero by the potion’s mana_amount."""
        hero.mana_bar.gainMana(self.mana_amount)