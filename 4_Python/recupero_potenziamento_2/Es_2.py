# Funzione per leggere un intero positivo (0 non valido qui)
def leggi_intero_positivo(messaggio):
    while True:
        try:
            val = float(input(messaggio))
            if not val.is_integer() or val < 0:  # modificato per permettere 0 qui
                raise ValueError
            return int(val)
        except ValueError:
            print("Errore: inserire un numero intero positivo (0 per terminare).")

# Leggo il numero x
x = leggi_intero_positivo("Inserisci il numero x (intero positivo): ")

sequenza = []
print("Inserisci la sequenza di interi positivi (0 per terminare):")

while True:
    num = leggi_intero_positivo("Numero: ")
    if num == 0:
        break
    sequenza.append(num)

# QUI: fine ciclo, ora stampo e analizzo la sequenza

print("\nSequenza inserita:", sequenza)

occ = sequenza.count(x)

if occ == 1:
    print(f"Il numero {x} compare 1 sola volta nella sequenza.")
else:
    print(f"Il numero {x} compare {occ} volte nella sequenza.")

if x in sequenza:
    posizione = sequenza.index(x) + 1
    print(f"Il numero {x} compare per la prima volta in posizione {posizione} nella sequenza.")
else:
    print(f"Il numero {x} non compare nella sequenza.")

somma_diversi = 0
for n in sequenza:
    if n != x:
        somma_diversi += n

print(f"La somma dei valori della sequenza diversi da {x} è {somma_diversi}.")
