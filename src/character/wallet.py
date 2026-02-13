class Wallet:
    def __init__(self, gold: int = 0):
        self.gold = gold

    def add_gold(self, amount: int):
        self.gold += amount

    def spend_gold(self, amount: int) -> bool:
        if self.gold >= amount:
            self.gold -= amount
            return True
        return False
