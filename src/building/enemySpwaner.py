from src.building.mine import Mine
from src.building.monsterFactory import MonsterFactory


class EnemySpawner:
    def __init__(self,mine : "Mine" ):
        self.mine = mine
        self.factory = MonsterFactory()

    def spawn_enemies(self):
        enemies = []
        for i in range(self.mine.level_manager.get_nb_monsters()):
            enemies.append(MonsterFactory.create_monster())
        self.mine.monsters = enemies
