from abc import ABC, abstractmethod
from src.item.usableItem import UsableItem
from src.character.hero import Hero

class Potion(UsableItem, ABC):
    def __init__(self, name: str, owner: Hero):
        super().__init__(name, owner)

    def use(self):
        """Call the potion’s effect on the owner and remove it from inventory."""
        self.apply_effects(self.owner)
        self.owner.inventory.remove_item(self)
        self.owner = None

    @abstractmethod
    def apply_effects(self, hero: Hero):
        """Each concrete potion defines its effect on the hero."""
        pass
