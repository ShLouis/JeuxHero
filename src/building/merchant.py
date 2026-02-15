from typing import List
from building import Building
from src.character.hero import Hero
from src.item.item import Item


class Merchant(Building):
    name = "Merchant"
    description = "At the merchant, you can pay gold to buy items."

    def __init__(self,shop:List[Item]):
        self.shop = shop

    def enter(self, hero):
        print(f"Welcome to the {self.name} !")
        print("Here are the available items:\n")
        while True:
            for index, item in enumerate(self.shop, start=1):
                print(f"{index}. {item.name} - {item.price} gold")
            choice = input("\nEnter the number of the item you want to buy (or 'q' to leave): ")
            if choice.lower() == 'q':
                print("You leave the merchant.")
                break
            if not choice.isdigit():
                print("Please enter a valid number.")
                continue
            choice = int(choice)
            if 1 <= choice <= len(self.shop):
                selected_item = self.shop[choice - 1]
                self.sell(hero, selected_item)
            else:
                print("Please enter a valid number.")

    def sell(self,hero:Hero,item:Item):
        if hero.wallet.spend_gold(item.price):
            hero.inventory.add_item(item)
            print(f"Remaining gold: {hero.wallet.gold}")
        else:
            print(f"{hero.name} doesn't have enough gold to buy {item.name}!")
