import random
import time

class Character:
    def __init__(self, name, hp_range, damage_range, special_ability, story):
        self.name = name
        self.max_hp = random.randint(hp_range[0], hp_range[1])
        self.hp = self.max_hp
        self.damage = random.randint(damage_range[0], damage_range[1])
        self.special_ability = special_ability
        self.story = story
        self.coins = 0
        self.charity_donation = 0
        self.special_ability_cooldown = 0
        self.items = []

    def attack(self):
        return self.damage

    def use_special_ability(self):
        pass

    def introduce(self):
        print(self.story)
        time.sleep(0.5)

    def add_coins(self, amount):
        self.coins += amount
        print(f"Found {amount} coins! Total coins: {self.coins}")
        time.sleep(0.5)

    
class Barbarian(Character):
    def __init__(self):
        super().__init__("Barbarian", (120, 150), (100, 120), "Killing Blow", 
                         "You are a strong warrior who wants to be the greatest warrior of all time!")
        self.killing_blow_cooldown = 0

    def use_special_ability(self):
        if self.killing_blow_cooldown <= 0:
            base_chance = 0.1  # Base 10% chance for Killing Blow
            charity_bonus = self.charity_donation * 0.02  # 2% increase per coin donated
            if random.random() < base_chance + charity_bonus:
                print("Killing Blow activated!")
                self.killing_blow_cooldown = 2  # 2-turn cooldown
                return 300
        else:
            print("Killing Blow is on cooldown.")
        return 0

    def choose_attack(self):
        print("Choose an attack:")
        time.sleep(0.5)
        print("1. Double Swing (1.5x damage)")
        time.sleep(0.5)
        print("2. Axe Swing (normal damage)")
        time.sleep(0.5)
        print("3. Whirlwind (chance to deal damage or fail)")
        time.sleep(0.5)
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            return self.double_swing()
        elif choice == "2":
            return self.axe_swing()
        elif choice == "3":
            return self.whirlwind()
        else:
            print("Invalid choice, defaulting to Axe Swing.")
            return self.axe_swing()

    def double_swing(self):
        if random.random() < 0.25:  # 25% chance to make monster skip next turn
            print("Barbarian's Double Swing intimidates the monster!")
            time.sleep(0.5)
            return self.damage * 1.5
        else:
            return self.damage * 1.5

    def axe_swing(self):
        return self.damage

    def whirlwind(self):
        if random.random() < 0.5:  # 50% chance
            print("Whirlwind successful!")
            time.sleep(0.5)
            return self.damage
        else:
            print("Whirlwind failed!")
            time.sleep(0.5)
            return 0

class Archer(Character):
    def __init__(self):
        super().__init__("Archer", (95, 110), (95, 105), "Dodge", 
                         "You are a banished elf who wants to atone for your guilt and return to the elf city.")
        self.dodge_cooldown = 0

    def dodge(self):
        if self.dodge_cooldown <= 0:
            base_chance = 0.2  # Base 20% chance for Dodge
            charity_bonus = self.charity_donation * 0.02  # 2% increase per coin donated
            if random.random() < base_chance + charity_bonus:
                print("Dodge activated!")
                self.dodge_cooldown = 2  # 2-turn cooldown
                return True
        else:
            print("Dodge is on cooldown.")
        return False

    def choose_attack(self):
        print("Choose an attack:")
        time.sleep(0.5)
        print("1. Double Arrow (2x damage)")
        time.sleep(0.5)
        print("2. Fire Arrow (1.5x damage)")
        time.sleep(0.5)
        print("3. Dagger (illusion effect)")
        time.sleep(0.5)
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            return self.double_arrow()
        elif choice == "2":
            return self.fire_arrow()
        elif choice == "3":
            return self.dagger()
        else:
            print("Invalid choice, defaulting to Fire Arrow.")
            return self.fire_arrow()

    def double_arrow(self):
        return self.damage * 2

    def fire_arrow(self):
        return self.damage * 1.5

    def dagger(self):
        if random.random() < 0.25:  # 25% chance to make monster miss next attack
            print("Archer's Dagger creates an illusion, causing the monster to miss its next attack!")
            time.sleep(0.5)
            return 0
        else:
            return self.damage

class Mage(Character):
    def __init__(self):
        super().__init__("Mage", (70, 90), (120, 150), "Killing Blow", 
                         "You are a great mage with a dream to become an archmage.")
        self.killing_blow_cooldown = 0

    def use_special_ability(self):
        if self.killing_blow_cooldown <= 0:
            base_chance = 0.1  # Base 10% chance for Killing Blow
            charity_bonus = self.charity_donation * 0.02  # 2% increase per coin donated
            if random.random() < base_chance + charity_bonus:
                print("Killing Blow activated!")
                self.killing_blow_cooldown = 2  # 2-turn cooldown
                return 300
        else:
            print("Killing Blow is on cooldown.")
        return 0

    def choose_attack(self):
        print("Choose an attack:")
        time.sleep(0.5)
        print("1. Fire Ball (2x damage)")
        time.sleep(0.5)
        print("2. Lightning Ball (2x damage, may hurt self)")
        time.sleep(0.5)
        print("3. Ice Bolt (may freeze the monster)")
        time.sleep(0.5)
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            return self.fire_ball()
        elif choice == "2":
            return self.lightning_ball()
        elif choice == "3":
            return self.ice_bolt()
        else:
            print("Invalid choice, defaulting to Ice Bolt.")
            return self.ice_bolt()

    def fire_ball(self):
        return self.damage * 2

    def lightning_ball(self):
        if random.random() < 0.2:  # 20% chance to hit self instead
            print("Lightning Ball backfired and hit the mage!")
            self.hp -= 10  # Mage takes 10 damage
            return self.damage * 2
        else:
            print("Lightning Ball missed the monster!")
            return 0

    def ice_bolt(self):
        if random.random() < 0.3:  # 30% chance to freeze the monster
            print("Ice Bolt froze the monster!")
            return 0
        else:
            return self.damage

# Items
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class HealingPotion(Item):
    def __init__(self):
        super().__init__("Healing Potion", "Heals 20 HP during combat.")

    def use(self, character):
        character.hp = min(character.hp + 20, character.max_hp)

class DamageBoost(Item):
    def __init__(self):
        super().__init__("Damage Boost", "Increases damage by 10 during combat.")

    def use(self, character):
        character.damage += 10
