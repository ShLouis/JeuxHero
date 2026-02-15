class LevelManager:
    def __init__(self, ):
        self.current_level = 1

    @staticmethod
    def fibonacci(n: int) -> int:
        if n == 1:
            return 1

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def get_nb_monsters(self):
        return LevelManager.fibonacci(self.current_level)

    def level_up(self):
        self.current_level += 1


