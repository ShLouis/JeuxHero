from typing import List

from building.building import Building
from building.enemySpwaner import EnemySpawner
from building.levelManager import LevelManager
from character.hero import Hero
from character.monster import Monster


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
        self.monsters = self.spawner.spawn_enemies()