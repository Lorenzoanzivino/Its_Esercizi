''' chiedere in input in quale posizione l'utentè è arrivato alla gara. a seconda della posizione aggiungi "st", "nd", "rd", "th"'''

position:int= int(input("Insert finishing position: "))

if position == 1:
    print(f"You're {position}st!")

elif position == 2:
    print(f"You're {position}nd!")

elif position == 3:
    print(f"You're {position}rd!")

else:
    print(f"You're {position}th!")


#Metodo Match
n:int= int(input("Digita la tua posizione: "))

match n:
    case 1:
        print(f" Sei {n} st")
    case 2: 
        print(f"Sei {n} nd")
    case 3:
        print(f"Sei {n} rd") 
    case _:
        print(f"Sei {n} th")