from typing import List

from src.building.building import Building
from src.building.enemySpwaner import EnemySpawner
from src.building.levelManager import LevelManager
from src.character.hero import Hero
from src.character.monster import Monster


class Mine(Building):
    name = "Mine"
    description = "A mine filled with monsters."

    def __init__(self,
                 level_manager: LevelManager,
                 spawner: EnemySpawner):
        self.level_manager = level_manager
        self.spawner = spawner
        self.monsters: List[Monster] = []

    def enter(self, hero: Hero) -> None:
        print(f"You enter the {self.name}.")
        current_level = self.level_manager.current_level
        print(f"Current level: {current_level}")
        nb_monsters = self.level_manager.get_nb_monsters()
        print(f"number of monsters: {nb_monsters}")
