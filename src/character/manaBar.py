class ManaBar:
    def __init__(self, max_mana: int):
        self.max_mana = max_mana
        self.mana = max_mana

    def spendMana(self, amount: int):
        self.mana = max(0, self.mana - amount)

    def gainMana(self, amount: int):
        self.mana = min(self.max_mana, self.mana + amount)

    def is_empty(self) -> bool:
        return self.mana <= 0
