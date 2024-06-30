import random
import time

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

    def attack(self):
        print(f"{self.name} swings its club wildly, trying to hit you!")
        return self.damage, False

class SkeletonWarrior(Monster):
    def __init__(self):
        super().__init__("Skeleton Warrior", 200, 30)

    def attack(self):
        if random.random() < 0.25:
            print(f"{self.name} blocks the attack with its shield!")
            return 0, False
        else:
            print(f"{self.name} slashes with its rusty sword, aiming for your weak spots!")
            return self.damage, False

class Goblin(Monster):
    def __init__(self):
        super().__init__("Goblin", 150, 20)

    def attack(self):
        print(f"{self.name} jumps around, trying to stab you with its dagger!")
        return self.damage, False

class Lich(Monster):
    def __init__(self):
        super().__init__("Lich", 450, 60)

    def attack(self):
        if random.random() < 0.5:
            print(f"{self.name} performs a killing blow!")
            return 300, False
        else:
            print(f"{self.name} casts a dark spell, draining your life force!")
            return self.damage, False
