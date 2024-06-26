import random
import time  # To simulate delays for a more immersive experience

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
        time.sleep(1)  # Delay for 1 second

    def add_coins(self, amount):
        self.coins += amount
        print(f"Found {amount} coins! Total coins: {self.coins}")
        time.sleep(1)  # Delay for 1 second

    def upgrade_max_hp(self, cost, increase):
        if self.coins >= cost:
            self.coins -= cost
            self.max_hp += increase
            self.hp = self.max_hp
            print(f"Upgraded max HP by {increase}.")
            print(f"Remaining coins: {self.coins}")
        else:
            print("Not enough coins to upgrade max HP.")
        time.sleep(1)  # Delay for 1 second

    def upgrade_damage(self, cost, increase):
        if self.coins >= cost:
            self.coins -= cost
            self.damage += increase
            print(f"Upgraded damage by {increase}.")
            print(f"Remaining coins: {self.coins}")
        else:
            print("Not enough coins to upgrade damage.")
        time.sleep(1)  # Delay for 1 second

    def donate_to_charity(self, amount):
        if self.coins >= amount:
            self.coins -= amount
            self.charity_donation += amount
            print(f"Donated {amount} coins to charity. Total donations: {self.charity_donation}")
        else:
            print("Not enough coins to donate to charity.")
        time.sleep(1)  # Delay for 1 second

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
        time.sleep(1)  # Delay for 1 second
        print("1. Double Swing (1.5x damage)")
        time.sleep(1)  # Delay for 1 second
        print("2. Axe Swing (normal damage)")
        time.sleep(1)  # Delay for 1 second
        print("3. Whirlwind (chance to deal damage or fail)")
        time.sleep(1)  # Delay for 1 second
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
            time.sleep(1)  # Delay for 1 second
            return self.damage * 1.5
        else:
            return self.damage * 1.5

    def axe_swing(self):
        return self.damage

    def whirlwind(self):
        if random.random() < 0.5:  # 50% chance
            print("Whirlwind successful!")
            time.sleep(1)  # Delay for 1 second
            return self.damage
        else:
            print("Whirlwind failed!")
            time.sleep(1)  # Delay for 1 second
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
        time.sleep(1)  # Delay for 1 second
        print("1. Double Arrow (2x damage)")
        time.sleep(1)  # Delay for 1 second
        print("2. Fire Arrow (1.5x damage)")
        time.sleep(1)  # Delay for 1 second
        print("3. Dagger (illusion effect)")
        time.sleep(1)  # Delay for 1 second
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
            time.sleep(1)  # Delay for 1 second
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
        time.sleep(1)  # Delay for 1 second
        print("1. Fire Ball (2x damage)")
        time.sleep(1)  # Delay for 1 second
        print("2. Lightning Ball (2x damage, may hurt self)")
        time.sleep(1)  # Delay for 1 second
        print("3. Ice Bolt (may freeze the monster)")
        time.sleep(1)  # Delay for 1 second
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
            time.sleep(1)  # Delay for 1 second
            self.hp -= self.damage * 2
        return self.damage * 2

    def ice_bolt(self):
        if random.random() < 0.25:  # 25% chance to freeze
            print("Ice Bolt freezes the monster!")
            time.sleep(1)  # Delay for 1 second
            return "freeze"
        else:
            return self.damage

class Monster:
    def __init__(self, name, hp, damage, special_ability=None):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.special_ability = special_ability
        self.special_ability_cooldown = 0

    def attack(self):
        return self.damage

    def use_special_ability(self):
        pass

class TrollWarlord(Monster):
    def __init__(self):
        super().__init__("Troll Warlord", 200, 25, "Double Swing")

    def attack(self):
        if self.special_ability_cooldown <= 0:
            if random.random() < 0.1:  # 10% chance for Double Swing
                print(f"{self.name} activates Double Swing!")
                time.sleep(1)  # Delay for 1 second
                self.special_ability_cooldown = 2  # 2-turn cooldown
                return self.damage * 1.5
        return self.damage

class RegularTroll(Monster):
    def __init__(self):
        super().__init__("Regular Troll", 150, 15)

class SkeletonWarrior(Monster):
    def __init__(self):
        super().__init__("Skeleton Warrior", 100, 20, "Block")
        self.block_chance = 0.3  # 30% chance to block an attack

    def attack(self):
        if self.special_ability_cooldown <= 0:
            if random.random() < 0.1:  # 10% chance to say something unclear
                self.say_something_unclear()
            return self.regular_attack()
        else:
            print(f"{self.name}'s {self.special_ability} is on cooldown.")
            time.sleep(1)  # Delay for 1 second
            self.special_ability_cooldown -= 1
            return 0

    def regular_attack(self):
        return self.damage

    def use_special_ability(self):
        if self.special_ability_cooldown <= 0:
            if random.random() < self.block_chance:
                print("Skeleton Warrior blocks the attack with its shield!")
                time.sleep(1)  # Delay for 1 second
                self.special_ability_cooldown = 2  # 2-turn cooldown
                return True
        return False

class Goblin(Monster):
    def __init__(self):
        super().__init__("Goblin", 50, 10)

class Lich(Monster):
    def __init__(self):
        super().__init__("Lich", 350, 50, "Killing Blow")
        self.killing_blow_chance = 0.5  # 50% chance for Killing Blow

    def attack(self):
        if self.special_ability_cooldown <= 0:
            if random.random() < 0.1:  # 10% chance to say something unclear
                self.say_something_unclear()
            return self.regular_attack()
        else:
            print(f"{self.name}'s {self.special_ability} is on cooldown.")
            time.sleep(1)  # Delay for 1 second
            self.special_ability_cooldown -= 1
            return 0

    def regular_attack(self):
        return self.damage

    def use_special_ability(self):
        if self.special_ability_cooldown <= 0:
            if random.random() < self.killing_blow_chance:
                print("Lich activates Killing Blow!")
                time.sleep(1)  # Delay for 1 second
                self.special_ability_cooldown = 2  # 2-turn cooldown
                return 300
        return 0

def choose_character():
    print("Welcome to the Text RPG game!")
    time.sleep(1)  # Delay for 1 second
    print("Choose your class:")
    time.sleep(1)  # Delay for 1 second
    print("1. Barbarian")
    time.sleep(1)  # Delay for 1 second
    print("2. Archer")
    time.sleep(1)  # Delay for 1 second
    print("3. Mage")
    time.sleep(1)  # Delay for 1 second
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        character = Barbarian()
    elif choice == "2":
        character = Archer()
    elif choice == "3":
        character = Mage()
    else:
        print("Invalid choice, defaulting to Barbarian.")
        character = Barbarian()

    character.introduce()
    return character

def relax(character):
    print(f"{character.name} relaxes and restores 5 HP.")
    time.sleep(1)  # Delay for 1 second
    character.hp = min(character.max_hp, character.hp + 5)
    character.add_coins(random.randint(20, 40))

def hit_the_road(character):
    events = [
        "meet_an_adventurer",
        "nothing_happens",
        "meet_a_monster",
        "find_shop"
    ]
    event = random.choices(events, weights=[0.2, 0.5, 0.2, 0.1], k=1)[0]
    
    if event == "meet_an_adventurer":
        print("You meet a friendly adventurer who restores your HP to the max!")
        time.sleep(1)  # Delay for 1 second
        character.hp = character.max_hp
    elif event == "nothing_happens":
        print("Nothing happens along the road.")
        time.sleep(1)  # Delay for 1 second
        character.add_coins(random.randint(20, 40))
    elif event == "meet_a_monster":
        print("You encounter a monster along the road!")
        time.sleep(1)  # Delay for 1 second
        monster = choose_monster()
        combat(character, monster)
    elif event == "find_shop":
        print("You find a shop!")
        time.sleep(1)  # Delay for 1 second
        visit_shop(character)

def choose_monster():
    monsters = [TrollWarlord(), RegularTroll(), SkeletonWarrior(), Goblin(), Lich()]
    return random.choice(monsters)

def combat(player, monster):
    while player.hp > 0 and monster.hp > 0:
        print(f"\n{player.name} attacks the {monster.name}!")
        time.sleep(1)  # Delay for 1 second
        
        if isinstance(player, Barbarian):
            damage = player.choose_attack()
            if random.random() < 0.25:  # 25% chance to make monster skip next turn after Double Swing
                print(f"{player.name} intimidates the monster, making it skip its next turn!")
                time.sleep(1)  # Delay for 1 second
                continue

        elif isinstance(player, Archer):
            damage = player.choose_attack()
            if damage == 0:  # If Dagger causes illusion effect
                print(f"{player.name} creates an illusion, causing the monster to miss its next attack!")
                time.sleep(1)  # Delay for 1 second
                continue

        elif isinstance(player, Mage):
            damage = player.choose_attack()
            if damage == "freeze":  # If Ice Bolt freezes the monster
                print(f"{player.name} freezes the monster, making it skip its next turn!")
                time.sleep(1)  # Delay for 1 second
                continue

        else:
            damage = player.attack()

        if isinstance(monster, SkeletonWarrior) and monster.use_special_ability():
            continue

        if player.hp <= 0:
            print(f"{player.name} has been defeated!")
            break

        monster.hp -= damage
        if monster.hp <= 0:
            print(f"{monster.name} has been defeated!")
            time.sleep(1)  # Delay for 1 second
            character.add_coins(random.randint(20, 40))
            break

        print(f"{player.name} has {player.hp} HP left.")
        time.sleep(1)  # Delay for 1 second

        print(f"\n{monster.name} attacks {player.name}!")
        time.sleep(1)  # Delay for 1 second
        
        if random.random() < 0.1:  # 10% chance to say something unclear
            monster.say_something_unclear()
            time.sleep(1)  # Delay for 1 second

        monster_damage = monster.attack()

        if isinstance(player, Archer) and player.dodge():
            print(f"{player.name} dodges the attack!")
            time.sleep(1)  # Delay for 1 second
            continue
        
        player.hp -= monster_damage

        print(f"{monster.name} has {monster.hp} HP left.")
        time.sleep(1)  # Delay for 1 second

        if player.hp <= 0:
            print(f"{player.name} has been defeated!")
            break

    if player.hp > 0:
        print(f"{monster.name} has been defeated!")
        time.sleep(1)  # Delay for 1 second
    else:
        print(f"{player.name} has been defeated!")
        time.sleep(1)  # Delay for 1 second

def visit_shop(character):
    print("Welcome to the shop!")
    time.sleep(1)  # Delay for 1 second
    print(f"You currently have {character.coins} coins.")
    time.sleep(1)  # Delay for 1 second
    print("1. Upgrade max HP by +10 (cost: 15 coins)")
    time.sleep(1)  # Delay for 1 second
    print("2. Upgrade damage by +10 (cost: 20 coins)")
    time.sleep(1)  # Delay for 1 second
    print("3. Donate to charity (variable cost)")
    time.sleep(1)  # Delay for 1 second
    print("4. Leave the shop")
    time.sleep(1)  # Delay for 1 second
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        character.upgrade_max_hp(15, 10)
    elif choice == "2":
        character.upgrade_damage(20, 10)
    elif choice == "3":
        amount = int(input("Enter the amount of coins you want to donate: "))
        character.donate_to_charity(amount)
    elif choice == "4":
        print("Leaving the shop.")
    else:
        print("Invalid choice.")

# Main game loop
character = choose_character()
while character.hp > 0:
    print("\nWhat would you like to do?")
    time.sleep(1)  # Delay for 1 second
    print("1. Hit the road")
    time.sleep(1)  # Delay for 1 second
    print("2. Relax and restore")
    time.sleep(1)  # Delay for 1 second
    print("3. Visit the shop")
    time.sleep(1)  # Delay for 1 second
    print("4. Quit")
    time.sleep(1)  # Delay for 1 second
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        hit_the_road(character)
    elif choice == "2":
        relax(character)
    elif choice == "3":
        visit_shop(character)
    elif choice == "4":
        print("Exiting the game.")
        break
    else:
        print("Invalid choice.")

print("Game over. Thanks for playing!")
