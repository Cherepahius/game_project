import random
import time

class Monster:
    def __init__(self, name, hp, damage):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.damage = damage
        self.cooldowns = {}

    def say_something_unclear(self):
        phrases = [
            "Grrr... Arrgh...",
            "Blargh... Hisss...",
            "Raaaaa...",
            "Hissss... Grooo...",
        ]
        print(f"{self.name} says: {random.choice(phrases)}")

    def attack(self):
        self.say_something_unclear()
        time.sleep(0.5)
        return self.damage, False

class TrollWarlord(Monster):
    def __init__(self):
        super().__init__("Troll Warlord", 400, 40)
    
    def attack(self):
        if self.cooldowns.get("double_swing", 0) == 0:
            if random.random() < 0.25:
                self.cooldowns["double_swing"] = 2
                print(f"{self.name} is so angry and eager that he performs a double swing!")
                return self.damage * 2, False
        self.cooldowns["double_swing"] = max(0, self.cooldowns.get("double_swing", 0) - 1)
        print(f"{self.name} performs a regular attack.")
        return super().attack()

class RegularTroll(Monster):
    def __init__(self):
        super().__init__("Regular Troll", 250, 25)

class SkeletonWarrior(Monster):
    def __init__(self):
        super().__init__("Skeleton Warrior", 200, 30)

    def attack(self):
        if random.random() < 0.25:
            print(f"{self.name} blocks the attack with his shield!")
            return 0, False
        print(f"{self.name} performs a regular attack.")
        return super().attack()

class Goblin(Monster):
    def __init__(self):
        super().__init__("Goblin", 150, 20)

class Lich(Monster):
    def __init__(self):
        super().__init__("Lich", 450, 60)
    
    def attack(self):
        if self.cooldowns.get("life_steal", 0) == 0:
            if random.random() < 0.25:
                self.cooldowns["life_steal"] = 2
                life_steal_amount = int(self.hp * 0.3)
                self.hp = min(self.max_hp, self.hp + life_steal_amount)
                print(f"{self.name} performs a life steal, dealing {life_steal_amount} damage and healing himself for the same amount!")
                return life_steal_amount, False
        self.cooldowns["life_steal"] = max(0, self.cooldowns.get("life_steal", 0) - 1)
        print(f"{self.name} performs a regular attack.")
        return super().attack()
