from character.monster import Monster


class TerrorOfTheDepths(Monster):
    def __init__(self, name: str = "TerrorOfTheDepths", max_health: int = 75, base_damage: int = 10, gold: int = 10):
        super().__init__(name, max_health, base_damage, gold)
