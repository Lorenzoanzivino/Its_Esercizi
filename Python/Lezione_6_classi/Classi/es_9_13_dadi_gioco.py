'''9-13. Dadi: Crea una classe Die con un attributo chiamato sides, che ha un valore predefinito di 6. Scrivi un metodo chiamato roll_die() che stampi un numero casuale tra 1 e il numero di lati che il dado ha. Crea un dado a 6 lati e lancialo 10 volte. Crea anche un dado a 10 lati e uno a 20 lati. Lanciali entrambi 10 volte.'''

import random 

class Dice:
    def __init__(self, sides:int = 6):
        self.sides = sides
    
    def roll_dice(self):
        roll = random.randint(1, self.sides)

        return roll
    

dice_6:Dice = Dice()
dice_10:Dice = Dice()
dice_20:Dice = Dice()

for i in range(1, 11):
    print(dice_6.roll_dice())

print("--------------------------")

for i in range(1, 11):
    print(dice_10.roll_dice())

print("--------------------------")

for i in range(1, 11):
    print(dice_20.roll_dice())

print("--------------------------")

