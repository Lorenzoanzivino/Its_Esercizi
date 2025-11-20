'''Sistema di Voti Scolastici:
Crea una funzione che prenda come input il nome di uno studente e i suoi punteggi nelle diverse materie. La funzione calcola la media dei punteggi e stampa il nome dello studente, la media e un messaggio che indica se lo studente ha superato l'esame (media >= 60) o se ha fallito. Crea un ciclo for per iterare su un elenco di studenti e punteggi, chiamando la funzione per ciascuno studente.'''


def studente(nome:str, voto:list[int]):
    somma = 0
    count = 0
    media = 0

    for i in voto:
        somma += i
        count += 1
    media = somma / count


    # Determina se lo studente ha superato o fallito
    if media >= 60:  # Usa 60 come valore per il superamento
        risultato = "Superato!"
    else:
        risultato = "Fallito!"
    
    # Restituisci un tuple con il nome, la media e il risultato
    return (nome, media, risultato)


# Chiama la funzione per calcolare la media e il risultato
result = studente("marco", [90, 70, 80])

# Stampa il risultato
print(f"Studente: {result[0]}, Media: {result[1]:.2f}, Risultato: {result[2]}")

list_of_students:list[dict] = [{'Marco': [90, 70, 80], 'lorenzo': [70, 70, 60], 'Antonio': [50, 70, 60]}]

for student in list_of_students:
    for nome, voto in student.items():
        result = studente(nome, voto)
        print(f"\nStudente: {result[0]}, Media: {result[1]:.2f}, Risultato: {result[2]}")