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

class RegularTroll(Monster):
    def __init__(self):
        super().__init__("Regular Troll", 250, 25)

class SkeletonWarrior(Monster):
    def __init__(self):
        super().__init__("Skeleton Warrior", 200, 30)

    def attack(self):
        if random.random() < 0.25:
            print(f"{self.name} blocks the attack with its shield!")
            return 0, False
        else:
            return self.damage, False

class Goblin(Monster):
    def __init__(self):
        super().__init__("Goblin", 150, 20)

class Lich(Monster):
    def __init__(self):
        super().__init__("Lich", 450, 60)

    def attack(self):
        if random.random() < 0.5:
            print(f"{self.name} performs a killing blow!")
            return 300, False
        else:
            return self.damage, False
