from character.monster import Monster


class Spider(Monster):
    def __init__(self, name: str = "Spider", max_health: int = 50, base_damage: int = 5, gold: int = 5):
        super().__init__(name, max_health, base_damage, gold)
