import random

class Monster:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self):
        return self.damage, False

class TrollWarlord(Monster):
    def __init__(self):
        super().__init__("Troll Warlord", 400, 40)

    def attack(self):
        if random.random() < 0.5:
            print("Troll Warlord is so angry and eager that he performs a double swing attack!")
            return self.damage * 2, False
        print("Troll Warlord roars and attacks!")
        return self.damage, False

class RegularTroll(Monster):
    def __init__(self):
        super().__init__("Regular Troll", 250, 25)

    def attack(self):
        print("Regular Troll grunts and attacks!")
        return self.damage, False

class SkeletonWarrior(Monster):
    def __init__(self):
        super().__init__("Skeleton Warrior", 200, 30)

    def attack(self):
        if random.random() < 0.3:
            print("Skeleton Warrior blocks your attack with its shield!")
            return 0, False
        print("Skeleton Warrior rattles its bones and attacks!")
        return self.damage, False

class Goblin(Monster):
    def __init__(self):
        super().__init__("Goblin", 150, 20)

    def attack(self):
        print("Goblin screeches and attacks!")
        return self.damage, False

class Lich(Monster):
    def __init__(self):
        super().__init__("Lich", 450, 60)

    def attack(self):
        if random.random() < 0.5:
            print("Lich cackles and attempts a killing blow!")
            return self.hp, False
        elif random.random() < 0.3:
            print("Lich uses Life Steal!")
            life_steal_amount = int(self.hp * 0.3)
            self.hp += life_steal_amount
            print(f"Lich heals for {life_steal_amount} HP.")
            return life_steal_amount, False
        print("Lich casts a dark spell and attacks!")
        return self.damage, False
