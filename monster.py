import random
import time

class Monster:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp 
        self.damage = damage
          

    def attack(self):
        return self.damage

class TrollWarlord(Monster):
    def __init__(self):
        super().__init__("Troll Warlord", 10, 10)

class RegularTroll(Monster):
    def __init__(self):
        super().__init__("Regular Troll", 10, 10)

class SkeletonWarrior(Monster):
    def __init__(self):
        super().__init__("Skeleton Warrior", 10, 10)

    def block_attack(self):
        if random.random() < 0.2:  # 20% chance to block attack
            print("Skeleton Warrior blocks the attack with its shield!")
            time.sleep(0.5)
            return True
        else:
            return False

class Goblin(Monster):
    def __init__(self):
        super().__init__("Goblin", 10, 10)

class Lich(Monster):
    def __init__(self):
        super().__init__("Lich", 10 , 10)

    def use_special_ability(self):
        if random.random() < 0.5:  # 50% chance for Killing Blow
            print("Lich summons dark energies for a deadly strike!")
            time.sleep(0.5)
            return 300
        return 0
