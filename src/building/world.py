from building.village import Village
from character.hero import Hero


class World:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(World, cls).__new__(cls)
        return cls._instance


    def __init__(self,village: Village,hero: Hero):
        self.village = village
        self.hero = hero