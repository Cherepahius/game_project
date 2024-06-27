class Potion():
    def __init__(self, strength: int) -> None:
        self.strength = strength
        self.name = "potion"
       
    def use(self):
        if self.strength == 1:
            return 20
        elif self.strength == 2:
            return 50
        else:
            return 999       
