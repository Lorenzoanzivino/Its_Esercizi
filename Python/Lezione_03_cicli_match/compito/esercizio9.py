'''Esercizio 9
Il valore di π può essere approssimato utilizzando la seguente serie infinita:
π = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...
Scrivere un programma che calcoli il valore di π utilizzando questa serie e determini quanti termini sono necessari per ottenere approssimazioni sempre più accurate.
Quindi:
• progettare un algoritmo che mostri in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14;
• modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.141;
• modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.1415;
• modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati per ottenere il valore di π ≈ 3.14159.
Nota: Il programma deve iterare fino a raggiungere ciascuna delle soglie indicate, contando il numero di termini necessari.'''

#per risolvere questo mi sono attenuto a un video youtube che spiegava la "SERIE INFINITA DI LEIBNIZ"

#inizializzo a zero una variabile pi greco
pi_greco:float = 0

#inizializzo a zero un contatore dei termini
contatore:int = 0

#inizializzo una variabile segni che utilizzerò per invertire il segno
segni:int = 1

#inizializzo una lista con le soglie da verificare
soglie:list[float] = [3.14,3.141, 3.1415, 3.14159]

#inizializzo una variabile booleana per verificare lo stato della soglia
soglia:bool = [False] * len(soglie)

#inizializzo a 1 il denominatore
denominatore:int= 1

#inizializzo un contatore per il conteggio delle soglie uguale alla lunghezza della lista soglie
contatore_soglie = len(soglie)

#ciclo While con condizione True se il contatore delle soglie è maggiore di 0
while contatore_soglie > 0:
    #operazione per il calcolo dell'approssimazione del pi greco, inverto il segno e aggiorno il contatore
    pi_greco += segni * (4/denominatore)
    segni *= -1
    contatore += 1
    #ciclo For per scorrere gli indice della lista e verifico quali soglie sono state raggiunte
    for i in range(len (soglie)):
        if not soglia[i] and (pi_greco >= soglie[i] and pi_greco <= soglie[i]+0.00001) :
            print (f"Per ottenere {soglie[i]} sono necessari {contatore} termini")
            soglia[i]= True
            contatore_soglie -= 1
    
    denominatore += 2