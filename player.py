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
        self.cooldowns = {
            "defensive_skill": 0,
            "special_attack": 0
        }
        self.defense_mode = False
        self.defense_rounds_left = 0


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
        attacks = self.available_attacks()
        print("\nChoose your attack:")
        for i, attack in enumerate(attacks, 1):
            print(f"{i}. {attack.replace('_', ' ').title()}")
        print(f"{len(attacks) + 1}. Use Defensive Skill")
        print(f"{i + 2}. Inventory")
        choice = int(input("Enter the number of your choice: "))
        if choice == len(attacks) + 1:
            return "use_defensive_skill"
        elif choice == i + 2:
            current_hp = self.hp
            self.view_inventory()
            new_hp = self.hp
            if new_hp > current_hp:
                print(new_hp > current_hp)
                return 1
            else:
                print(new_hp > current_hp)
                return 0
        elif choice >= len(attacks):
            print("Invalid choice, defaulting to Double Swing.")
            return attacks[0]
        else:
            return attacks[choice - 1]
            
              
    def apply_defensive_skill(self):
        if self.cooldowns["defensive_skill"] == 0:
            self.defense_mode = True
            self.defense_rounds_left = 2
            self.cooldowns["defensive_skill"] = 3
            self.activate_defensive_skill()
            return True
        else:
            print(f"Defensive skill is on cooldown. {self.cooldowns['defensive_skill']} turns remaining.")
            return False

    def update_defensive_mode(self):
        if self.defense_mode:
            self.defense_rounds_left -= 1
            if self.defense_rounds_left <= 0:
                self.defense_mode = False
                print(f"{self.name}'s defensive skill effect has ended.")
        
        for skill in self.cooldowns:
            if self.cooldowns[skill] > 0:
                self.cooldowns[skill] -= 1

    def activate_defensive_skill(self):
        pass

    def apply_defensive_skill(self):
        if self.cooldowns["defensive_skill"] == 0:
            self.defense_mode = True
            self.defense_rounds_left = 2
            self.cooldowns["defensive_skill"] = 3
            self.activate_defensive_skill()
            return True
        else:
            print(f"Defensive skill is on cooldown. {self.cooldowns['defensive_skill']} turns remaining.")
            return False

    def update_defensive_mode(self):
        if self.defense_mode:
            self.defense_rounds_left -= 1
            if self.defense_rounds_left <= 0:
                self.defense_mode = False
                print(f"{self.name}'s defensive skill effect has ended.")
        
        for skill in self.cooldowns:
            if self.cooldowns[skill] > 0:
                self.cooldowns[skill] -= 1

    def activate_defensive_skill(self):
        pass

class Barbarian(Player):
    def __init__(self):
        super().__init__("Barbarian", random.randint(220, 250), random.randint(110, 130), 0.1, 0.0)

    def double_swing(self):
        if self.cooldowns["special_attack"] == 0:
            self.cooldowns["special_attack"] = 2
            print(f"{self.name} used Double Swing!")
            return int(self.damage * 1.5), True
        print("Double Swing is on cooldown.")
        return 0, False

    def axe_swing(self):
        print(f"{self.name} used Axe Swing!")
        return self.damage, False

    def whirlwind(self):
        if self.cooldowns["special_attack"] == 0:
            self.cooldowns["special_attack"] = 2
            print(f"{self.name} used Whirlwind!")
            if random.random() < 0.5:
                return self.damage, False
            else:
                print("Whirlwind failed, and Barbarian got a headache.")
                return 0, False
        print("Whirlwind is on cooldown.")
        return 0, False

    def activate_defensive_skill(self):
        self.hp += 20
        self.defense_rounds_left = 2
        print(f"{self.name} used Fortitude! HP increased by 20 for 2 rounds.")

    def available_attacks(self):
        return ["double_swing", "axe_swing", "whirlwind"]

class Archer(Player):
    def __init__(self):
        super().__init__("Archer", random.randint(195, 210), random.randint(105, 115), 0.0, 0.1)

    def double_arrow(self):
        if self.cooldowns["special_attack"] == 0:
            self.cooldowns["special_attack"] = 2
            print(f"{self.name} used Double Arrow!")
            return int(self.damage * 2), False
        print("Double Arrow is on cooldown.")
        return 0, False

    def fire_arrow(self):
        if self.cooldowns["special_attack"] == 0:
            self.cooldowns["special_attack"] = 2
            print(f"{self.name} used Fire Arrow!")
            return int(self.damage * 1.5), False
        print("Fire Arrow is on cooldown.")
        return 0, False

    def dagger_attack(self):
        if self.cooldowns["special_attack"] == 0:
            self.cooldowns["special_attack"] = 2
            print(f"{self.name} used Dagger Attack!")
            if random.random() < 0.75:
                return self.damage, True
            else:
                print(f"{self.name} used Dagger Attack but it missed.")
                return 0, False
        print("Dagger Attack is on cooldown.")
        return 0, False

    def activate_defensive_skill(self):
        self.hp += 15
        self.defense_rounds_left = 2
        print(f"{self.name} used Shadow Cloak! HP increased by 15 for 2 rounds.")

    def available_attacks(self):
        return ["double_arrow", "fire_arrow", "dagger_attack"]

class Mage(Player):
    def __init__(self):
        super().__init__("Mage", random.randint(170, 190), random.randint(130, 150), 0.1, 0.0)

    def fire_ball(self):
        if self.cooldowns["special_attack"] == 0:
            self.cooldowns["special_attack"] = 2
            print(f"{self.name} used Fire Ball!")
            return int(self.damage * 2), False
        print("Fire Ball is on cooldown.")
        return 0, False

    def lightning_ball(self):
        if self.cooldowns["special_attack"] == 0:
            self.cooldowns["special_attack"] = 2
            print(f"{self.name} used Lightning Ball!")
            if random.random() < 0.5:
                print(f"{self.name} got struck by the lightning!")
                self.hp -= self.damage // 2
            return int(self.damage * 2), False
        print("Lightning Ball is on cooldown.")
        return 0, False

    def ice_bolt(self):
        if self.cooldowns["special_attack"] == 0:
            self.cooldowns["special_attack"] = 2
            print(f"{self.name} used Ice Bolt!")
            if random.random() < 0.25:
                return self.damage, True
            return self.damage, False
        print("Ice Bolt is on cooldown.")
        return 0, False

    def activate_defensive_skill(self):
        self.hp += 10
        self.defense_rounds_left = 2
        print(f"{self.name} used Ice Barrier! HP increased by 10 for 2 rounds.")

    def available_attacks(self):
        return ["fire_ball", "lightning_ball", "ice_bolt"]