'''3) Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 2, 4, 6, 8, 10, 12, 14
b) 1, 4, 7, 10, 13
c) 30, 25, 20, 15, 10, 5, 0
d) 5, 15, 25, 35, 45'''

# Ciclo For versione Estesa
print(f"A)...")
for i in range(2, 15, 2):
    print(i)
print(f"\nB)...")
for i in range(1, 14, 3):
    print(i)
print(f"\nC)...")
for i in range(30, -1, -5):
    print(i)
print(f"\nD)...")
for i in range(5, 46, 10):
    print(i)

# Ciclo For versione Compatta 
print("A.1)", *list(range(2, 15, 2)))
print("B.1)", *list(range(1, 14, 3)))
print("C.1)", *list(range(30, -1, -5)))
print("D.1)", *list(range(5, 46, 10)))


# Ciclo While
print(f"A2)...")
i:int = 2
while i <= 14:
    print(i)
    i += 2
print(f"\nB2)...")
i:int = 1
while i <= 13:
    print(i)
    i += 3
print(f"\nC2)...")
i:int = 30
while i > 0:
    print(i)
    i -= 5
print(f"\nD2)...")
i:int = 5
while i <= 45:
    print(i)
    i += 10