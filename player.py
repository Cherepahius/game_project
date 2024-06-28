import random
import time

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

    def add_coins(self, amount):
        self.coins += amount
        print(f"You found {amount} coins! You now have {self.coins} coins.")

    def gain_experience(self, amount):
        self.experience += amount
        print(f"You gained {amount} experience points! Total EXP: {self.experience}")
        if self.experience >= self.level * 100:
            self.level_up()

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
        choice = int(input("Enter the number of your choice: ")) - 1
        if 0 <= choice < len(self.attacks):
            return self.attacks[choice]['method']
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
