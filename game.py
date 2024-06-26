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

    def upgrade_max_hp(self, cost, increase):
        if self.coins >= cost:
            self.coins -= cost
            self.max_hp += increase
            self.hp = self.max_hp
            print(f"Upgraded max HP by {increase}.")
            print(f"Remaining coins: {self.coins}")
        else:
            print("Not enough coins to upgrade max HP.")
        time.sleep(0.5)

    def upgrade_damage(self, cost, increase):
        if self.coins >= cost:
            self.coins -= cost
            self.damage += increase
            print(f"Upgraded damage by {increase}.")
            print(f"Remaining coins: {self.coins}")
        else:
            print("Not enough coins to upgrade damage.")
        time.sleep(0.5)

    def donate_to_charity(self, amount):
        if self.coins >= amount:
            self.coins -= amount
            self.charity_donation += amount
            print(f"Donated {amount} coins to charity. Total donations: {self.charity_donation}")
        else:
            print("Not enough coins to donate to charity.")
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
        if random.random() < 0.5:  # 50% chance
            print("Lightning Ball hit both the monster and the Mage!")
            time.sleep(0.5)
            self.hp -= self.damage * 2
        return self.damage * 2

    def ice_bolt(self):
        if random.random() < 0.25:  # 25% chance to freeze
            print("Ice Bolt freezes the monster!")
            time.sleep(0.5)
            return "freeze"
        else:
            return self.damage

class Monster:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp + 100  # Increased HP by 100
        self.damage = damage + 10  # Increased damage by 10

    def attack(self):
        return self.damage

class TrollWarlord(Monster):
    def __init__(self):
        super().__init__("Troll Warlord", 400, 40)

class RegularTroll(Monster):
    def __init__(self):
        super().__init__("Regular Troll", 250, 25)

class SkeletonWarrior(Monster):
    def __init__(self):
        super().__init__("Skeleton Warrior", 200, 30)

    def block_attack(self):
        if random.random() < 0.2:  # 20% chance to block attack
            print("Skeleton Warrior blocks the attack with its shield!")
            time.sleep(0.5)
            return True
        else:
            return False

class Goblin(Monster):
    def __init__(self):
        super().__init__("Goblin", 150, 20)

class Lich(Monster):
    def __init__(self):
        super().__init__("Lich", 450, 60)

    def use_special_ability(self):
        if random.random() < 0.5:  # 50% chance for Killing Blow
            print("Lich summons dark energies for a deadly strike!")
            time.sleep(0.5)
            return 300
        return 0

# Main game logic
def choose_character():
    print("Welcome to the Text-based RPG!")
    time.sleep(0.5)
    print("Choose your character:")
    time.sleep(0.5)
    print("1. Barbarian")
    time.sleep(0.5)
    print("2. Archer")
    time.sleep(0.5)
    print("3. Mage")
    time.sleep(0.5)
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        return Barbarian()
    elif choice == "2":
        return Archer()
    elif choice == "3":
        return Mage()
    else:
        print("Invalid choice, defaulting to Barbarian.")
        return Barbarian()

def hit_the_road(character):
    print("Hitting the road...")
    time.sleep(0.5)
    result = random.random()
    if result < 0.05:  # 5% chance to meet an adventurer
        print("You meet a fellow adventurer who restores your HP to the maximum!")
        character.hp = character.max_hp
    elif result < 0.55:  # 50% chance nothing happens
        print("Nothing eventful happens.")
        found_coins = random.randint(1, 5)
        character.add_coins(found_coins)
    else:  # 40% chance to meet a monster
        print("A wild monster appears!")
        time.sleep(0.5)
        monster = random.choice([TrollWarlord(), RegularTroll(), SkeletonWarrior(), Goblin(), Lich()])
        combat(character, monster)

def combat(character, monster):
    print(f"A wild {monster.name} appears!")
    time.sleep(0.5)

    while character.hp > 0 and monster.hp > 0:
        # Character's turn
        if character.special_ability_cooldown <= 0:
            if isinstance(character, Barbarian) and random.random() < 0.1:
                damage = character.use_special_ability()
            elif isinstance(character, Mage) and random.random() < 0.1:
                damage_or_freeze = character.use_special_ability()
                if damage_or_freeze == "freeze":
                    print(f"The {monster.name} is frozen and skips its turn!")
                    time.sleep(0.5)
                    continue
                else:
                    damage = damage_or_freeze
            else:
                damage = character.choose_attack()

            if damage > 0:
                print(f"You hit the {monster.name} for {damage} damage!")
                time.sleep(0.5)
                monster.hp -= damage

        character.special_ability_cooldown -= 1

        if monster.hp <= 0:
            print(f"You have defeated the {monster.name}!")
            time.sleep(0.5)
            loot_coins = random.randint(2, 10)
            character.add_coins(loot_coins)
            break

        # Monster's turn
        if isinstance(monster, Lich) and random.random() < 0.05:
            damage = monster.use_special_ability()
        else:
            damage = monster.attack()

        if isinstance(character, Archer) and random.random() < 0.25:
            if character.dodge():
                print("You dodged the attack!")
                time.sleep(0.5)
                continue

        if isinstance(monster, SkeletonWarrior):
            if monster.block_attack():
                print(f"The {monster.name} blocks your attack!")
                time.sleep(0.5)
                continue

        print(f"The {monster.name} attacks you for {damage} damage!")
        time.sleep(0.5)
        character.hp -= damage

    if character.hp <= 0:
        print("You have been defeated...")
        time.sleep(0.5)

# Game setup
character = choose_character()
character.introduce()

while character.hp > 0:
    print("\nWhat would you like to do?")
    time.sleep(0.5)
    print("1. Hit the road")
    time.sleep(0.5)
    print("2. Quit")
    time.sleep(0.5)
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        hit_the_road(character)
    elif choice == "2":
        print("Exiting the game.")
        break
    else:
        print("Invalid choice.")

print("Game over. Thanks for playing!")
