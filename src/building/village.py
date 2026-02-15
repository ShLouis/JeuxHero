from typing import List
from building.building import Building


class Village():
    def __init__(self, buildings: List[Building]):
        self.buildings = buildings