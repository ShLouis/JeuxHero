from character.monster import Monster


class Zombie(Monster):
    def __init__(self, name: str = "Zombie", max_health: int = 60, base_damage: int = 7, gold: int = 7):
        super().__init__(name, max_health, base_damage, gold)
