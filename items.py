import time

class Potion():
    def __init__(self, strength: int) -> None:
        self.strength = strength
        if strength == 1:
            self.name = "Potion"
            self.price = 10
        elif strength == 2:
            self.name = "Greater Potion"
            self.price = 25
        else:
            self.name = "Full Potion"
            self.price = 50
            
       
    def use(self):
        if self.strength == 1:
            return 25
        elif self.strength == 2:
            return 75
        else:
            return 999       


class Equipment():
    def __init__(self, identity: int) -> None:
        self.identity = identity
        if self.identity == 1:
            self.name = "Cheap Weapon"
            self.price = 5
        elif self.identity == 2:
            self.name = "Strong Weapon"
            self.price = 20
        elif self.identity == 3:
            self.name = "Magic Weapon"
            self.price = 50
        elif self.identity == 4:
            self.name = "Cheap Armor"
            self.price = 5
        elif self.identity == 5:
            self.name = "Strong Armor"
            self.price = 20
        else:
            self.name = "Magic Armor"
            self.price = 50

        
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
        


class Store():
    def __init__(self) -> None:
        self.potions_for_sale = [Potion(1), Potion(2), Potion(3)]
        self.list_of_equipment = [Equipment(1), Equipment(2), Equipment(3), Equipment(4), Equipment(5), Equipment(6)]
        self.inventory = {
            self.potions_for_sale[0].name : self.potions_for_sale[0].price,
            self.potions_for_sale[1].name : self.potions_for_sale[1].price,
            self.potions_for_sale[2].name : self.potions_for_sale[2].price,
            self.list_of_equipment[0].name : self.list_of_equipment[0].price,
            self.list_of_equipment[1].name : self.list_of_equipment[1].price,
            self.list_of_equipment[2].name : self.list_of_equipment[2].price,
            self.list_of_equipment[3].name : self.list_of_equipment[3].price,
            self.list_of_equipment[4].name : self.list_of_equipment[4].price,
            self.list_of_equipment[5].name : self.list_of_equipment[5].price
            }
        
    def view_store(self):
        store_menu = 1
        print("Welcome to the shop, here are our wares")
        time.sleep(0.5)
        for key, value in self.inventory.items():
            print(f"{store_menu}. {key} : {value} Coins")
            store_menu += 1
            time.sleep(0.5)
        