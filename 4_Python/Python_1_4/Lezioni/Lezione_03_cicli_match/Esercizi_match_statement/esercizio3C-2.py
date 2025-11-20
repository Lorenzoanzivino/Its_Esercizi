'''Esercizio 3C-2.
Scrivere un programma in Python che converta un voto di laurea italiano (sistema in 110-emi) nel sistema GPA americano (scala 0-4).
Il programma deve accettare in input un voto di laurea compreso tra 66 e 110, espresso come numero intero e usare un match per determinare il corrispondente GPA americano, secondo questa tabella di conversione:

- 106-110 → 4.0
- 101-105 → 3.7
- 96-100 → 3.3
- 91-95 → 3.0
- 86-90 → 2.7
- 81-85 → 2.3
- 76-80 → 2.0
- 70-75 → 1.7
- 66-69 → 1.0
- Altro caso → "Voto non valido"

Expected Output:

Inserisci il voto di laurea: 110
Output: GPA 4.0

- - - - - - - - - - - - - - - - -

Inserisci il voto di laurea: 65
Output: Voto non valido'''

voto_laurea:int = int(input("Inserisci un voto, compreso tra 66 e 110: "))
GPA:list[int] = [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.0]

match voto_laurea:
    case voto_laurea if voto_laurea > 105 and voto_laurea < 111:
        print(f"GPA {GPA[0]}")
    case voto_laurea if voto_laurea > 100 and voto_laurea < 106:
        print(f"GPA {GPA[1]}")
    case voto_laurea if voto_laurea > 95 and voto_laurea < 101:
        print(f"GPA {GPA[2]}")
    case voto_laurea if voto_laurea > 90 and voto_laurea < 96:
        print(f"GPA {GPA[3]}")
    case voto_laurea if voto_laurea > 85 and voto_laurea < 91:
        print(f"GPA {GPA[4]}")
    case voto_laurea if voto_laurea > 80 and voto_laurea < 86:
        print(f"GPA {GPA[5]}")
    case voto_laurea if voto_laurea > 75 and voto_laurea < 81:
        print(f"GPA {GPA[6]}")
    case voto_laurea if voto_laurea >69 and voto_laurea < 76:
        print(f"GPA {GPA[7]}")
    case voto_laurea if voto_laurea > 65 and voto_laurea < 70:
        print(f"GPA {GPA[8]}")
    case _:
        print("Voto non valido")