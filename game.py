import random
import time
from player import Barbarian, Archer, Mage
from monster import TrollWarlord, RegularTroll, SkeletonWarrior, Goblin, Lich
from items import Store, Equipment

def display_forest():
    forest_art = """
      ///\\\///\\\///\\\///\\\
     ////\\\\////\\\\////\\\\
    /////\\\\\/////\\\\\/////\\\\\
    /////\\\\/////\\\\/////\\\\
    """
    print(forest_art)
    time.sleep(1)

def display_city():
    city_art = """
      _____||_____
     /////////////\\
    ///////////////\\
   |    _    _    ||
   |[] | |  | | [] ||
   |   | |  | |    ||
   |   | |  | |    ||
   |   |_|  |_|    ||
   |      __       ||
   |     |  |      ||
  /|[]   |  |  []  |\\
 / |    _|  |_     | \\
    """
    print(city_art)
    time.sleep(1)
def game_setup():
    print("Welcome to the adventure game!")
    time.sleep(0.5)
    print("Choose your character class:")
    time.sleep(0.5)
    print("1. Barbarian")
    time.sleep(0.5)
    print("2. Archer")
    time.sleep(0.5)
    print("3. Mage")
    time.sleep(0.5)
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        player = Barbarian()
        print("You are a strong warrior who wants to be the greatest warrior of all time!")
    elif choice == "2":
        player = Archer()
        print("You are a banished elf who wants to atone for your guilt and return to the elf city.")
    elif choice == "3":
        player = Mage()
        print("You are a great mage with a dream to become an archmage.")
    else:
        print("Invalid choice, defaulting to Barbarian.")
        player = Barbarian()

    player.introduce()
    return player

def encounter_monster(player):
    monsters = [TrollWarlord(), RegularTroll(), SkeletonWarrior(), Goblin(), Lich()]
    monster = random.choice(monsters)
    print(f"A wild {monster.name} appears!")
    time.sleep(0.5)

    while player.hp > 0 and monster.hp > 0:
        print(f"{player.name} HP: {player.hp}/{player.max_hp}")
        print(f"{monster.name} HP: {monster.hp}")
        player.update_defensive_mode()
        attack_choice = player.choose_attack()
        
        
       
        if attack_choice == 0:
            continue
        elif attack_choice == 1:
            print(f"{player.name} used a potion and now has HP: {player.hp}/{player.max_hp}")
            damage_dealt = 0
            enemy_stunned = False
        elif attack_choice == "use_defensive_skill":
            damage_dealt = 0
            enemy_stunned = False
            if not player.apply_defensive_skill():
                continue
        else:
            attack_method = getattr(player, attack_choice, None)
            if attack_method:
                damage_dealt, enemy_stunned = attack_method()
            else:
                print(f"Invalid attack choice: {attack_choice}")
                continue

            if random.random() < player.killing_blow_chance:
                print(f"{player.name} landed a killing blow!")
                damage_dealt = 300

        monster.hp -= damage_dealt
        print(f"{monster.name} HP left: {monster.hp}")

        if monster.hp <= 0:
            coins_found = random.randint(2, 10)
            player.add_coins(coins_found)
            exp_gained = 50
            player.gain_experience(exp_gained)
            print(f"You defeated the {monster.name} and gained {coins_found} coins and {exp_gained} experience points!")
            break

        if not enemy_stunned:
            if isinstance(player, Archer) and random.random() < player.dodge_chance:
                print(f"{player.name} dodged the attack!")
                monster_attack = 0
            else:
                monster_attack, player_stunned = monster.attack()
                if random.random() < player.dodge_chance:
                    print(f"{player.name} dodged the attack!")
                    monster_attack = 0

            player.hp -= monster_attack
            print(f"{player.name} HP left: {player.hp}")

        else:
            print(f"The {monster.name} is stunned and misses its turn!")

        if player.hp <= 0:
            print(f"You were defeated by the {monster.name}.")
            break

def main_game_loop(player):
    turns = 0
    while True:
        print("You're traveling through the wilds")
        print("What would you like to do?")
        time.sleep(0.5)
        print("1. Hit the road")
        time.sleep(0.5)
        print("2. Relax and recover")
        time.sleep(0.5)
        print("3. Check Stats")
        time.sleep(0.5)
        print("4. Check Inventory")
        time.sleep(0.5)
        print("5. Quit the game")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            display_forest()
            turns += 1
            if random.random() < 0.05:
                player.hp = player.max_hp
                print("You met a friendly adventurer who restored your HP to the max!")
            elif random.random() < 0.4:
                encounter_monster(player)
                if player.hp <= 0:
                    print("Game over!")
                    break
            elif random.random() < 0.5:
                coins_found = random.randint(1, 5)
                player.add_coins(coins_found)
            else:
                print("Nothing happened.")

            if turns >= 5:
                print("You have reached the city!")
                city(player)
                turns = 0

        elif choice == "2":
            if random.random() <= 0.70:
                player.hp = min(player.max_hp, player.hp + 5)
                print(f"You relaxed and recovered. Current HP: {player.hp}/{player.max_hp}")
            else:
                print("A monster attacked you!")
                time.sleep(0.5)
                encounter_monster(player)
                if player.hp <= 0:
                    print("Game over!")
                    break

        elif choice == "3":
            player.view_stats()
        elif choice == "4":
            player.view_inventory()
        elif choice == "5":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

def city(player):
    display_city()
    city_name = ["King's Landing", "Minas Tirith", "Camelot", "Lothlórien", "Stormwind", "Baldur's Gate", "Rivendell", "Braavos", "Whiterun", "Hyrule Castle Town"]
    city_turns = 10
    while city_turns > 0:
        print(f"You reached the city of {random.choice(city_name)}. What would you like to do?")
        time.sleep(0.5)
        print("1. Go to the tavern")
        time.sleep(0.5)
        print("2. Go to the shop")
        time.sleep(0.5)
        print("3. Go to the city square")
        time.sleep(0.5)
        print("4. Leave the city")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            print("Welcome to the tavern! You can restore your HP to the maximum for 20 coins.")
            tavern_choice = input("Would you like to restore your HP? (yes/no): ")
            if tavern_choice.lower() == "yes" and player.coins >= 20:
                player.hp = player.max_hp
                player.coins -= 20
                print(f"Your HP is now fully restored. Current HP: {player.hp}/{player.max_hp}")
            elif tavern_choice.lower() == "yes" and player.coins < 20:
                print("You don't have enough coins.")
            else:
                print("You decided not to restore your HP.")
        elif choice == "2":
            shop = Store()
            shop.view_store()
            shop_choice = input(f"Please input the Item you would like to buy: ")
            if shop_choice.isdigit():
                if int(shop_choice) <= 3 and int(shop_choice) > 0:
                    if player.coins >= shop.potions_for_sale[int(shop_choice) - 1].price:
                        player.add_item(shop.potions_for_sale[int(shop_choice) - 1])
                        player.coins -= shop.potions_for_sale[int(shop_choice) - 1].price
                    else:
                        print("You don't have the coins to buy that")
                elif int(shop_choice) <= 9:
                    if player.coins >= shop.list_of_equipment[int(shop_choice) - 4].price:
                        player.add_equipment(shop.list_of_equipment[int(shop_choice) - 4])
                        player.coins -= shop.list_of_equipment[int(shop_choice) - 4].price
                    else:
                        print("You don't have the coins to buy that")
                else:
                    print("You decided not to buy anything")
        elif choice == "3":
            if city_turns > 0:
                event_chance = random.random()
                if event_chance < 0.25:
                    coins_lost = random.randint(1, 10)
                    player.coins = max(0, player.coins - coins_lost)
                    print(f"Rogues stole {coins_lost} coins! Current coins: {player.coins}")
                elif event_chance < 0.25:
                    hp_lost = random.randint(5, 15)
                    player.hp = max(0, player.hp - hp_lost)
                    print(f"Warriors punched you and you lost {hp_lost} HP! Current HP: {player.hp}/{player.max_hp}")
                else:
                    coins_found = random.randint(5, 15)
                    player.add_coins(coins_found)
                    #print(f"You found {coins_found} coins in the city square!")
                city_turns -= 1
            else:
                print("You have used all your turns in the city square.")
        elif choice == "4":
            print("You leave the city and continue your adventure.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    player = game_setup()
    main_game_loop(player)
