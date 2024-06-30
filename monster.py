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

    def attack(self):
        print(f"{self.name} is so angry and eager that it makes an RKO out of nowhere, dealing damage!")
        return self.damage, False

class RegularTroll(Monster):
    def __init__(self):
        super().__init__("Regular Troll", 250, 25)
        self.loot = random.randint(1,3)
        if self.loot < 3:
            self.loot = Equipment(1)
        else:
            self.loot = Equipment(5)
        


    def attack(self):
        print(f"{self.name} swings its club wildly, trying to hit you!")
        return self.damage, False

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
            print(f"{self.name} slashes with its rusty sword, aiming for your weak spots!")
            return self.damage, False

class Goblin(Monster):
    def __init__(self):
        super().__init__("Goblin", 150, 20)
        self.loot = Equipment(1)

    def attack(self):
        print(f"{self.name} jumps around, trying to stab you with its dagger!")
        return self.damage, False

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
            print(f"{self.name} casts a dark spell, draining your life force!")
            return self.damage, False
