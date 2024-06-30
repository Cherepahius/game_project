import random
import time
from items import Potion

class Player:
    def __init__(self, name, max_hp, damage, killing_blow_chance=0, dodge_chance=0):
        self.name = name
        self.hp = max_hp
        self.max_hp = max_hp
        self.damage = damage
        self.killing_blow_chance = killing_blow_chance
        self.dodge_chance = dodge_chance
        self.coins = 0
        self.experience = 0
        self.level = 1
        self.inventory = [Potion(1)]


    def view_stats(self):
        print (f"level {self.level}\n{self.experience} XP\n you need another {(self.level * 100) - self.experience} to go up a level\n{self.hp} / {self.max_hp} HP\n{self.coins} Coins\nand {self.damage} Strangth")
        time.sleep(0.5)
    
    def add_item(self, item):
        self.inventory.append(item)
        print(f"You got a {item.name}")
        time.sleep(0.5)

    def add_equipment(self, equipment):
        upgrade = equipment.use()
        if "Weapon" in equipment.name:
            self.damage += upgrade
            print(f"You got {equipment.name}, your damage increases to {self.damage}")
        elif "Armor" in equipment.name:
            self.max_hp += upgrade
            self.hp += upgrade
            print(f"You got {equipment.name}, your HP increases to {self.max_hp}")

    def add_coins(self, amount):
        self.coins += amount
        print(f"You found {amount} coins! You now have {self.coins} coins.")

    def gain_experience(self, amount):
        self.experience += amount
        print(f"You gained {amount} experience points! Total EXP: {self.experience}")
        if self.experience >= self.level * 100:
            self.level_up()

    def view_inventory(self):
        if len(self.inventory) <= 0:
            print("you currently don't have anything in your inventory")
            time.sleep(0.5)
        else:
            for key, value in enumerate(self.inventory):
                print(f"{key + 1} : {value.name}")
                time.sleep(0.5)
            player_input = input("Pick an item: ")
            if player_input.isdigit():
                self.use_potion(int(player_input) - 1)
            else:
                pass

    def use_potion(self, player_input):
            if int(player_input) <= (len(self.inventory)):
                if self.hp < self.max_hp:
                    potion = self.inventory[player_input].use()
                    self.inventory.pop(player_input)
                    if potion < 999:
                        self.hp += potion
                        if self.hp > self.max_hp:
                            self.hp = self.max_hp
                    else:
                        self.hp = self.max_hp
                else:
                    print("Can't use a potion while your health is full")
                    time.sleep(0.5)
            else:
                pass

    def level_up(self):
        self.level += 1
        self.max_hp += 20
        self.damage += 5
        self.hp = self.max_hp
        self.experience = 0
        print(f"You leveled up! You are now level {self.level}. Max HP: {self.max_hp}, Damage: {self.damage}")

    def introduce(self):
        print(f"You are a {self.name} with {self.hp} HP and {self.damage} damage.")

    def choose_attack(self):
        print("Choose your attack:")
        time.sleep(0.5)
        for idx, attack in enumerate(self.attacks, 1):
            print(f"{idx}. {attack['name']}")
        print(f"{idx + 1}. Inventory")
        choice = input("Enter the number of your choice: ")
        if choice.isdigit():
            choice = int(choice) - 1
            if 0 <= choice < len(self.attacks):
                return self.attacks[choice]['method']
            elif choice == len(self.attacks):
                current_hp = self.hp
                self.view_inventory()
                new_hp = self.hp
                if new_hp > current_hp:
                    return 1
                else:
                    return 0
            else:
                print("Invalid choice, defaulting to Double Swing.")
                return self.attacks[0]['method']
        else:
            print("Invalid choice, defaulting to Double Swing.")
            return self.attacks[0]['method']

class Barbarian(Player):
    def __init__(self):
        super().__init__("Barbarian", random.randint(120, 150), random.randint(100, 120), killing_blow_chance=0.05)
        self.attacks = [
            {"name": "Double Swing", "method": "double_swing"},
            {"name": "Axe Swing", "method": "axe_swing"},
            {"name": "Whirlwind", "method": "whirlwind"}
        ]

    def double_swing(self):
        print(f"{self.name} used Double Swing!")
        return self.damage * 1.5, True

    def axe_swing(self):
        print(f"{self.name} used Axe Swing!")
        return self.damage, False

    def whirlwind(self):
        if random.random() < 0.5:
            print(f"{self.name} used Whirlwind!")
            return self.damage, False
        else:
            print(f"{self.name} used Whirlwind but only got a headache!")
            return 0, False

class Archer(Player):
    def __init__(self):
        super().__init__("Archer", random.randint(95, 110), random.randint(95, 105), dodge_chance=0.05)
        self.attacks = [
            {"name": "Double Arrow", "method": "double_arrow"},
            {"name": "Fire Arrow", "method": "fire_arrow"},
            {"name": "Dagger Attack", "method": "dagger_attack"}
        ]

    def double_arrow(self):
        print(f"{self.name} used Double Arrow!")
        return self.damage * 2, False

    def fire_arrow(self):
        print(f"{self.name} used Fire Arrow!")
        return self.damage * 1.5, False

    def dagger_attack(self):
        print(f"{self.name} used Dagger Attack!")
        if random.random() < 0.25:
            print(f"{self.name} uses Dagger Attack and makes the enemy miss!")
            return self.damage, True
        else:
            return self.damage, False

class Mage(Player):
    def __init__(self):
        super().__init__("Mage", random.randint(70, 90), random.randint(120, 150), killing_blow_chance=0.05)
        self.attacks = [
            {"name": "Fireball", "method": "fireball"},
            {"name": "Lightning Ball", "method": "lightning_ball"},
            {"name": "Ice Bolt", "method": "ice_bolt"}
            
        ]

    def fireball(self):
        print(f"{self.name} used Fireball!")
        return self.damage * 2, False

    def lightning_ball(self):
        print(f"{self.name} used Lightning Ball!")
        if random.random() < 0.5:
            print(f"{self.name} uses Lightning Ball and it backfires!")
            self.hp -= self.damage * 0.5
            return self.damage * 2, False
        else:
            return self.damage * 2, False

    def ice_bolt(self):
        print(f"{self.name} used Ice Bolt!")
        if random.random() < 0.25:
            print(f"{self.name} uses Ice Bolt and freezes the enemy!")
            return self.damage, True
        else:
            return self.damage, False
