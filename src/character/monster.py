from src.character.character import Character


class Monster(Character):
    def __init__(self, name: str = "Monster", max_health: int = 50, base_damage: int = 5, gold: int = 5):
        super().__init__(name, max_health, base_damage, gold)
