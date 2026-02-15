from building.building import Building


class Inn(Building):
    name = "Inn"
    description = "At the inn, you can pay gold to restore your health."
    price = 30

    def enter(self, hero):
        print(f"Welcome to the {self.name} !")
        print(f"You can pay {self.price} gold to fully restore your health.")

        choice = input("Do you want to pay ? (y/n) : ")

        if choice.lower() == "y":
            if hero.wallet.spend_gold(self.price):
                hero.health_bar.heal(hero.health_bar.max_health-hero.health_bar.health)
                print("You have been healed !")
                print(f"HP : {hero.health_bar.health}/{hero.health_bar.max_health}")
                print(f"Gold : {hero.wallet.gold}")
            else:
                print("Not enough gold !")
        else:
            print("You leave the inn.")