'''Esercizio 3C-10. Scrivere un programma in Python che permetta all'utente di inserire una data (giorno e mese espressi in forma numerica), salvi la data in una tupla e utilizzi un match statement per verificare se la data corrisponde a una festività o a un evento speciale:

- Capodanno → 1 Gennaio → "Capodanno"
- San Valentino → 14 Febbraio → "San Valentino"
- Festa della Repubblica Italiana → " Giugno → "Festa della Repubblica Italiana"
- Ferragosto → 15 Agosto → "Ferragosto"
- Halloween → 31 Ottobre → "Halloween"
- Natale → 25 Dicembre → "Natale"
- Altro caso → "Nessuna festività importante in questa data."

Expected Output:

Inserisci il giorno: 25
Inserisci il mese: 12
Output: Il 25/12 è Natale!

- - - - - - - - - - - - - - -

Inserisci il giorno: 5
Inserisci il mese: 3
Output: Nessuna festività importante in questa data.'''


mesi:dict[str, int] = {"gennaio": 1, "febbraio": 2, "marzo": 3, "aprile": 4, "maggio": 5, "giugno": 6, "luglio": 7, "agosto": 8, "settembre": 9, "ottobre": 10, "novembre": 11, "dicembre": 12}

g: int = int(input("Inserisci un giorno in forma numerica: "))
m: int = input("Inserisci un mese o in forma numerica o testuale: ")

if m.isdigit():
    m:int = int(m)
# associo il nome del mese al numero corrispondente
elif m in mesi:
    m:int = mesi[m]
else:
    print("Mese non valido")

m_30:list[int] = [4, 6, 9, 11]
m_31:list[int] = [1, 3, 5, 7, 8, 10, 12]

data: tuple[int] = (g, m)

# La funzione per printare in output il mese del mese associata al numero
def nome_mese(m:int):
    # RICERCA INVERSA 
    for mese, numero in mesi.items(): 
        if numero == m:
            return mese
    
    return "unknown"
    
match data:
    case (g, m_30) if g <= 0 or g > 31:
        print(f"Il {g} non esiste nel mese di {nome_mese(m)}")
    case (g, 2) if g <= 0 or g > 28:
        print(f"Il {g} non esiste nel mese di {nome_mese(m)}")
    case (g, m_31) if g <= 0 or g > 30:
        print(f"Il {g} non esiste nel mese di {nome_mese(m)}")
    case (1, 1):
        print(f"Il {g}/{m} è: Capodanno!")
    case (14, 2):
        print(f"Il {g}/{m} è: San Valentino!")
    case (2, 6):
        print(f"Il {g}/{m} è: Festa della Repubblica Italiana!")
    case (15, 8):
        print(f"Il {g}/{m} è: Ferragosto!")
    case (31, 10):
        print(f"Il {g}/{m} è: Halloween!")
    case (25, 12):
        print(f"Il {g}/{m} è: Natale!")
    case _:
        print("Nessuna festività importante in questa data.")


