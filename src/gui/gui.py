import os

from src.character.hero import Hero


class Gui:
    @staticmethod
    def show_game_setup():
        print("Welcome traveler, the village needs your help!")
        print("Monsters have coming up from the mines and attacking the villagers!")
        print("We need you to go down there and kill them.")
        print("What is your name, traveller?")

        name = input("Enter your hero's name: ")

        hero_choice = None
        Gui.clear()
        while hero_choice not in ["1", "2", "3"]:
            print("\nChoose your hero type:")
            print("0. View the Heros perks")
            print("1. Warrior")
            print("2. Paladin")
            print("3. Wizard")
            hero_choice = input("Choose your hero type: ")
            if hero_choice == "0":
                Gui.clear()
                Gui.show_hero_perks()
                hero_choice = None
            elif hero_choice not in ["1", "2", "3"]:
                Gui.clear()
                print("Invalid choice! Please choose 1, 2, or 3.")
        Gui.clear()
        return name, hero_choice

    @staticmethod
    def show_hero_perks():
        print("\n=== HERO PERKS ===")
        print("Warrior:")
        print(" - Deals 50% extra damage")

        print("\nPaladin:")
        print(" - Can equip shields to reduce incoming damage with shield")

        print("\nWizard:")
        print(" - 20% chance to dodge attacks")

    @staticmethod
    def clear():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def show_player_stats(hero: "Hero"):
        stats = hero.get_stats()

        print(f"\n=== {stats['name']}'s STATS ===")
        print(f"Health: {stats['health']}")
        print(f"Wallet: {stats['gold']} gold")
        print(f"Base damage: {stats['base_damage']}")

        if stats.get("weapon"):
            weapon = stats["weapon"]
            print(f"Weapon: {weapon['name']} (+{weapon['damage']} damage)")
        else:
            print("Weapon: None")

        if stats.get("shield"):
            shield = stats["shield"]
            print(f"Shield: {shield['name']} (+{shield['defense']} defense)")
        else:
            print("Shield: None")

        if len(hero.inventory.items) > 0:
            print("Inventory:")
            for i, item in enumerate(hero.inventory.items, start=1):
                print(f"  {i}. {item.name}")
        else:
            print("Inventory: empty")






