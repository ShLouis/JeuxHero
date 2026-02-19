from character.monster import Monster


class FinalBoss(Monster):
    def __init__(self, name: str = "Final Boss", max_health: int = 10, base_damage: int = 20, gold: int = 50):
        super().__init__(name, max_health, base_damage, gold)
