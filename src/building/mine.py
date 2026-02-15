from building import Building
from src.building.levelManager import LevelManager
from src.character.hero import Hero
from src.building.enemySpwaner import EnemySpawner


class Mine(Building):
    name = "Mine"
    description = "In the Mine you can kill monsters to earn gold."

    def __init__(self, ):
        self.level_manager = LevelManager()
        self.spawner = EnemySpawner(self)
        self.monsters = self.spawner.spawn_enemies()

    def enter(self, hero: "Hero"):
        ...
