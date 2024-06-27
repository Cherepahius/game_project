import time
import random
from player import Barbarian, Archer, Mage
from monster import TrollWarlord, RegularTroll, SkeletonWarrior, Goblin, Lich

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
                print(f"Player's HP: {character.hp}, Monster's HP: {monster.hp}")

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
        print(f"Player's HP: {character.hp}, Monster's HP: {monster.hp}")

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
