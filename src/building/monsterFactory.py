from src.character.monster import Monster


class MonsterFactory:
    @staticmethod
    def create_monster():
        return Monster()

