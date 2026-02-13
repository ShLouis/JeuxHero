class HealthBar:
    def __init__(self, max_health: int):
        self.max_health = max_health
        self.health = max_health

    def lose_health(self, amount: int):
        self.health = max(0, self.health - amount)

    def heal(self, amount: int):
        self.health = min(self.max_health, self.health + amount)

    def is_empty(self) -> bool:
        return self.health <= 0
