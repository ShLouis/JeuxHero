class Level:
    def __init__(self, xp: int = 0, level: int = 1,owner: Hero):
        self.xp = xp
        self.level = level
        self.owner = owner

    def gain_xp(self, amount: int):
        self.xp += amount
        if self.xp >= 10:
            self.level_up()

    def level_up(self):
        self.xp -= 10
        self.level += 1