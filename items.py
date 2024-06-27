class Potion():
    def __init__(self, strength: int) -> None:
        self.strength = strength
        if strength == 1:
            self.name = "Potion"
            self.price = 15
        elif strength == 2:
            self.name = "Greater Potion"
            self.price = 35
        else:
            self.name = "Full Potion"
            self.price = 50
            
       
    def use(self):
        if self.strength == 1:
            return 20
        elif self.strength == 2:
            return 50
        else:
            return 999       


class Equipment():
    def __init__(self, identity: int) -> None:
        self.identity = identity
        if self.identity == 1:
            self.name = "Cheap Weapon"
            self.price = 10
        elif self.identity == 2:
            self.name = "Strong weapon"
            self.price = 40
        elif self.identity == 3:
            self.name = "Magic Weapon"
            self.price = 100
        elif self.identity == 4:
            self.name = "Cheap Armor"
            self.price = 10
        elif self.identity == 5:
            self.name = "Strong Armor"
            self.price = 40
        else:
            self.name = "Magic Armor"
            self.price = 100

        
    def use(self):
        if self.identity == 1:
            return 2
        elif self.identity == 2:
            return 5
        elif self.identity == 3:
            return 10
        elif self.identity == 4:
            return 2
        elif self.identity == 5:
            return 5
        else:
            return 10