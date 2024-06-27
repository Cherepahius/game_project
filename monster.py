import random
import time

class Monster:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp 
        self.damage = damage + 10 

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
        super().__init__("Lich", 550, 70)

    def use_special_ability(self):
        if random.random() < 0.5:  # 50% chance for Killing Blow
            print("Lich summons dark energies for a deadly strike!")
            time.sleep(0.5)
            return 300
        return 0
