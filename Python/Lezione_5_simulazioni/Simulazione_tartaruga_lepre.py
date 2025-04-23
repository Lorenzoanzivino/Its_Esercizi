''' Requisiti del Codice:
- Utilizzare il modulo random per la generazione dei numeri casuali.
- Definire e utilizzare:
    - una funzione per visualizzare le posizioni sulla corsia di gara,
    - una funzione per calcolare la mossa della tartaruga,
    - una funzione per calcolare la mossa della lepre.
- Implementare un loop per simulare i tick dell'orologio. Ad ogni tick, calcolare le mosse, mostrare la posizione sulla corsia di gara, e determinare l'eventuale fine della gara.'''

'''# 1) Inizializzazione delle variabili:
    • pos_tartaruga = 1  # posizione iniziale della tartaruga
    • pos_lepre = 1      # posizione iniziale della lepre
    • percorso = lista di 70 caratteri '_' # percorso con 70 posizioni vuote
3) Funzione per visualizzare il percorso:
    • Creare una funzione che accetta il percorso e visualizza la corsia di gara
    • Ogni volta che la tartaruga e la lepre si trovano sulla stessa posizione, stampare "OUCH!!!"
    • Usare il carattere 'T' per la tartaruga, 'H' per la lepre, e '_' per le posizioni vuote.
4) Funzione per calcolare la mossa della tartaruga:
    • Generare un numero casuale (i) da 1 a 10.
    • Se 1 ≤ i ≤ 5, la tartaruga avanza di 3 quadrati ("passo veloce").
    • Se 6 ≤ i ≤ 7, la tartaruga arretra di 6 quadrati ("scivolata"), ma non può andare sotto il quadrato 1.
    • Se 8 ≤ i ≤ 10, la tartaruga avanza di 1 quadrato ("passo lento").
    • Restituire la nuova posizione della tartaruga, assicurandosi che non scenda sotto 1.
5) Funzione per calcolare la mossa della lepre:
    • Generare un numero casuale (j) da 1 a 10.
    • Se 1 ≤ j ≤ 2, la lepre non si muove ("riposo").
    • Se 3 ≤ j ≤ 4, la lepre avanza di 9 quadrati ("grande balzo").
    • Se 5 ≤ j ≤ 6, la lepre arretra di 12 quadrati ("grande scivolata"), ma non può andare sotto il quadrato 1.
    • Se 7 ≤ j ≤ 9, la lepre avanza di 1 quadrato ("piccolo balzo").
    • Se 10, la lepre arretra di 2 quadrati ("piccola scivolata"), ma non può andare sotto il quadrato 1.
    • Restituire la nuova posizione della lepre, assicurandosi che non scenda sotto 1.
6) Ciclo della gara (Tick dell'orologio):
    • Iniziare un ciclo infinito che simula i tick dell'orologio.
        1) Calcolare la mossa della tartaruga usando la funzione per la tartaruga.
        2) Calcolare la mossa della lepre usando la funzione per la lepre.
        3) Aggiornare il percorso con la nuova posizione della tartaruga e della lepre.
        4) Se tartaruga e lepre sono nella stessa posizione, inserire "OUCH!!!" nel percorso.
        5) Chiamare la funzione per visualizzare il percorso aggiornato.
7) Controllo se uno dei concorrenti ha vinto:
    • Se la posizione della tartaruga è >= 70:
        • Stampare "TORTOISE WINS! || VAY!!!" e terminare il ciclo.
    • Se la posizione della lepre è >= 70:
        • Stampare "HARE WINS || YUCH!!!" e terminare il ciclo.
    • Se entrambi raggiungono o superano il quadrato 70 nello stesso tick:
        • Stampare "IT'S A TIE." e terminare il ciclo.
8) Se nessuno ha vinto, ripetere il ciclo per il prossimo tick'''

import random

# 1) Inizializzazione delle variabili
pos_tartaruga:int = 1
pos_lepre:int = 1
percorso_lista:list = ['_'] * 70  # Il percorso è composto da 70 caselle

# Aggiungo la Stamina
stamina_T:int = 100
stamina_H:int = 100

# Ostacoli
ostacoli:dict[int] = {15:-3, 30:-5, 45:-7}

# Bonus
bonus:dict[int] = {10:+5, 30:+3, 50:+10}

# 2) Funzione per visualizzare il percorso
def percorso():
    percorso_visibile = percorso_lista[:]  # Copia della lista

    '''Assegna il valore 'T' alla posizione dell'array percorso_visibile che si trova all'indice pos_tartaruga - '''
    percorso_visibile[pos_tartaruga - 1] = 'T'  # Aggiungi 'T' per la tartaruga
    percorso_visibile[pos_lepre - 1] = 'H'  # Aggiungi 'H' per la lepre nelle loro posizioni
    
    # Stampare il percorso
    print(''.join(percorso_visibile))
    
    # Se tartaruga e lepre sono sulla stessa posizione
    if pos_tartaruga == pos_lepre:
        print("OUCH!!!")

# 3) Funzione per calcolare la mossa della tartaruga
def mossa_T(pos_tartaruga, piove, stamina_T, ostacoli, bonus):
    i = random.randint(1, 10)
    print(f"Mossa tartaruga: {i}")

    if 1 <= i <= 5:  # Passo veloce
        if stamina_T >= 5:  # Controlla se la stamina è sufficiente per muoversi
            pos_tartaruga += 3
            stamina_T -= 5  # Spendo stamina per muovermi
            if stamina_T < 0:  # Se la stamina scende sotto 0
                stamina_T = 0         
            print(f"Stamina rimasta: {stamina_T}")

        else:  # Se la stamina è insufficiente
            print("Non hai energia per muoverti. Il turno è saltato.")
            stamina_T += 10  # Ricarica stamina
            if stamina_T > 100:  # Se la stamina supera 100
                stamina_T = 100            
            print("Energia ricaricata di 10")


    elif 6 <= i <= 7:  # Scivolata
        if stamina_T >= 10:
            pos_tartaruga -= 6
            stamina_T -= 10
            if stamina_T < 0:  # Se la stamina scende sotto 0
                stamina_T = 0   
            print(f"Stamina rimasta: {stamina_T}")

            if pos_tartaruga < 1:
                pos_tartaruga = 1

        else:  # Se la stamina è insufficiente
            print("Non hai energia per muoverti. Il turno è saltato.")
            stamina_T += 10  # Ricarica stamina
            if stamina_T > 100:  # Se la stamina supera 100
                stamina_T = 100               
            print("Energia ricaricata di 10")

    elif 8 <= i <= 10:  # Passo lento
        if stamina_T >= 3:
            pos_tartaruga += 1
            stamina_T -= 3
            if stamina_T < 0:  # Se la stamina scende sotto 0
                stamina_T = 0   
            print(f"Stamina rimasta: {stamina_T}")

        else:  # Se la stamina è insufficiente
            print("Non hai energia per muoverti. Il turno è saltato.")
            stamina_T += 10  # Ricarica stamina
            if stamina_T > 100:  # Se la stamina supera 100
                stamina_T = 100               
            print("Energia ricaricata di 10")

    # BONUS: Verifica se la posizione della tartaruga corrisponde a una chiave nel dizionario dei BONUS
    if pos_tartaruga in bonus:  # Se la posizione è una chiave nel dizionario
        avanzamento = bonus[pos_tartaruga]  # Ottieni il valore (avanzamento) associato alla posizione
        pos_tartaruga += avanzamento  # Applica la avanzamento (decrementa la posizione)
        print(f"Bonus! La tartaruga avanza di {avanzamento} posizioni.")
        if pos_tartaruga > 70:
            pos_tartaruga = 70  # Non può avanzare oltre 70

    # OSTACOLO: Verifica se la posizione della tartaruga corrisponde a una chiave nel dizionario degli OSTACOLI
    if pos_tartaruga in ostacoli:  # Se la posizione è una chiave nel dizionario
        retrocessione = ostacoli[pos_tartaruga]  # Ottieni il valore (retrocessione) associato alla posizione
        pos_tartaruga += retrocessione  # Applica la retrocessione (decrementa la posizione)
        print(f"Ostacolo! La tartaruga retrocede di {retrocessione} posizioni.")
        if pos_tartaruga < 1:
            pos_tartaruga = 1  # Non può scendere sotto 1

    # METEO: Se piove, la tartaruga perde 1 posizione
    if piove:
        pos_tartaruga -= 1
        if pos_tartaruga < 1:  # Non può andare sotto 1
            pos_tartaruga = 1
    
    # Assicurati che la posizione non vada oltre la fine del percorso
    if pos_tartaruga > 70:  # Non può superare la fine del percorso
        pos_tartaruga = 70
    
    return pos_tartaruga, stamina_T

# 4) Funzione per calcolare la mossa della lepre
def mossa_L(pos_lepre, piove, stamina_H, ostacoli, bonus):
    j = random.randint(1, 10)
    print(f"\nMossa lepre: {j}")
    
    if 1 <= j <= 2:  # Riposo
        if stamina_H < 100:  # La lepre recupera stamina solo se non è al massimo
            stamina_H += 10
            if stamina_H > 100:  # Non può superare 100
                stamina_H = 100
            print(f"Stamina lepre dopo riposo: {stamina_H}")
        else:
            print("La lepre è già a piena energia, non ha bisogno di riposare.")

    elif 3 <= j <= 4:  # Grande balzo
        pos_lepre += 9
        stamina_H -= 15

    elif 5 <= j <= 6:  # Grande scivolata
        pos_lepre -= 12
        stamina_H -= 20
        if pos_lepre < 1:
            pos_lepre = 1

    elif 7 <= j <= 9:  # Piccolo balzo
        pos_lepre += 1
        stamina_H -= 5

    elif j == 10:  # Piccola scivolata
        pos_lepre -= 2
        stamina_H -= 8
        if pos_lepre < 1:
            pos_lepre = 1
    
    if stamina_H < 0:
        stamina_H = 0
    print(f"Stamina rimasta: {stamina_H}")   

    # BONUS: Verifica se la posizione della tartaruga corrisponde a una chiave nel dizionario dei BONUS
    if pos_lepre in bonus:  # Se la posizione è una chiave nel dizionario
        avanzamento = bonus[pos_lepre]  # Ottieni il valore (avanzamento) associato alla posizione
        pos_lepre += avanzamento  # Applica la avanzamento (decrementa la posizione)
        print(f"Bonus! La Lepre avanza di {avanzamento} posizioni.")
        if pos_lepre > 70:
            pos_lepre = 70  # Non può avanzare oltre 70

    # OSTACOLO: Verifica se la posizione della tartaruga corrisponde a una chiave nel dizionario degli ostacoli
    if pos_lepre in ostacoli:  # Se la posizione è una chiave nel dizionario
        retrocessione = ostacoli[pos_lepre]  # Ottieni il valore (retrocessione) associato alla posizione
        pos_lepre += retrocessione  # Applica la retrocessione (decrementa la posizione)
        print(f"Ostacolo! La tartaruga retrocede di {retrocessione} posizioni.")
        if pos_lepre < 1:
            pos_lepre = 1  # Non può scendere sotto 1
    
    # METEO: Se piove, la tartaruga perde 1 posizione 
    if piove:
        pos_lepre -= 1
        if pos_lepre < 1:  # Non può andare sotto 1
            pos_lepre = 1
    
    if pos_lepre > 70:  # Non può superare la fine del percorso
        pos_lepre = 70
    
    return pos_lepre, stamina_H

# 5) Ciclo della gara (Tick dell'orologio)
tick = 1  # Iniziamo con il primo tick

while True:
    print(f"\nTick: {tick}")  # Mostra il numero di tick
    
    # Meteo
    if (tick // 10) % 2 == 0:  # Ogni 10 tick si alterna
        print('sole')
        piove = False
    else:
        print('piove')
        piove = True

    # 1) Calcolare la mossa della tartaruga
    pos_tartaruga, stamina_T = mossa_T(pos_tartaruga, piove, stamina_T, ostacoli, bonus)
    print(f"Posizione tartaruga: {pos_tartaruga}")
    
    # 2) Calcolare la mossa della lepre
    pos_lepre, stamina_H = mossa_L(pos_lepre, piove, stamina_H, ostacoli, bonus)
    print(f"Posizione lepre: {pos_lepre}")
    
    # 3) Aggiornare e visualizzare il percorso
    percorso()
    
    # 4) Condizione di fine gara: se uno dei due raggiunge la fine
    if pos_tartaruga >= 70 and pos_lepre >= 70:
        print("\nIT'S A TIE.")
        break  # Termina il ciclo in caso di pareggio
    
    if pos_tartaruga >= 70:
        print("\nTORTOISE WINS! || VAY!!!")
        break  # Termina il ciclo se la tartaruga vince
    
    if pos_lepre >= 70:
        print("\nHARE WINS || YUCH!!!")
        break  # Termina il ciclo se la lepre vince

    tick += 1  # Aumentiamo il contatore dei tick
