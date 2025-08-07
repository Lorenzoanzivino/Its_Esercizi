# 09 if


print("\nif semplice")
x:int = 5
if x < 10:
    print("1- x è minore di 10")
print("1.1- Sono fuori dall'if")


print("\noperatori di comparazione")
y:int = 10
z:int = 4
if y == 10:
    print("2- y è uguale a 10")
if z != 10:
    print("2.1- z è diverso da 10")


print("\nElif - Else")
x:int = 12
if x < 10:
    print("3- x è minore di 10")
elif x == 10:
    print("3.1- x è uguale a 10")
else:
    print("3.2- x è maggiore di 10")


print("\noperatori logici AND e OR")
x: int = 15
if x > 10 and x < 20:
    print("x è compreso tra 10 e 20")
else:
    print("x non è compreso")

y:int = 12
z:int = 18
if y > 10 and z < 20:
    print("y è maggiore di 10 E z è minore di 20")
if z > 10 or z < 15:
    print("y è maggiore di 10 MA z non è minore di 15")


print("\nversione short hand")
x:int = 15
if x > 10 : print("x è maggiore di 10") # vale solo con un solo print
'''oppure'''
print("x è maggiore di 10") if x > 10 else print("x è minore di 10")

print("\nif innestati (annidati)")
x:int = 8
if x % 2 == 0:
    print("numero pari")
    if(x < 10):
        print("numero minore di 10")
else:
    print("numero dispari")