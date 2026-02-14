class Inventory:
    def __init__(self,spaces = 10):
        self.items = []
        self.spaces = spaces

    def is_full(self):
        return len(self.items) >= self.spaces

    def get_item(self, index):
        return self.items[index]

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, index):
        return self.items.pop(index)
