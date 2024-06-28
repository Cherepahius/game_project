import random
import time
from items import Equipment


class Monster:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.special_cooldown = 0

    def attack(self):
        if random.random() < 0.5:
            print(f"{self.name} mumbles something unclear...")
        return self.damage, False

class TrollWarlord(Monster):
    def __init__(self):
        super().__init__("Troll Warlord", 400, 40)
        self.loot = random.randint(1,3)
        if self.loot < 3:
            self.loot = Equipment(2)
        else:
            self.loot = Equipment(5)

    def double_swing(self):
        if self.special_cooldown == 0:
            self.special_cooldown = 2
            return self.damage * 2, True
        else:
            return self.attack()

class RegularTroll(Monster):
    def __init__(self):
        super().__init__("Regular Troll", 250, 25)
        self.loot = random.randint(1,3)
        if self.loot < 3:
            self.loot = Equipment(1)
        else:
            self.loot = Equipment(5)
        


class SkeletonWarrior(Monster):
    def __init__(self):
        super().__init__("Skeleton Warrior", 200, 30)
        self.loot = random.randint(1,2)
        if self.loot == 1:
            self.loot = Equipment(1)
        else:
            self.loot = Equipment(4)

    def attack(self):
        if random.random() < 0.25:
            print(f"{self.name} blocks from attacks with its shield!")
            return 0, False
        else:
            return self.damage, False

class Goblin(Monster):
    def __init__(self):
        super().__init__("Goblin", 150, 20)
        self.loot = Equipment(1)

class Lich(Monster):
    def __init__(self):
        super().__init__("Lich", 450, 60)
        self.loot = random.randint(1,2)
        if self.loot == 1:
            self.loot = Equipment(3)
        else:
            self.loot = Equipment(6)

    def attack(self):
        if random.random() < 0.5:
            print(f"{self.name} performs a killing blow!")
            return 300, False
        else:
            return self.damage, False
