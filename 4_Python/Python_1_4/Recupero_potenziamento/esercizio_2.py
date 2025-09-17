'''
lista1: 1, 2, 3, 4, 5

lista2: "Armatura", "Bravura", "Cane", "Diamante", "Elefante", "Furfante"
'''

def printListBackward(list:list, i=0):
    if i < len(list):                     
        printListBackward(list, i + 1)
        print(list[i])               




lista1 = [1, 2, 3, 4, 5]
lista2 = ["Armatura", "Bravura", "Cane", "Diamante", "Elefante", "Furfante"]

printListBackward(lista1)
print()
printListBackward(lista2)
