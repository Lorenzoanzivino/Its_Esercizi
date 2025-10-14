'''Crea un dizionario vuoto e aggiungi elementi
Scrivi una funzione aggiungi_studente(diz, nome, voto) che prende un dizionario vuoto o già esistente e aggiunge la coppia {nome: voto}.
Alla fine stampa il dizionario aggiornato.'''
def add_student(dizionario: dict, nome: str, voto: int):
    if nome in dizionario:
        # studente già presente → aggiorna il voto
        dizionario[nome] = voto
        print(f"Studente {nome} aggiornato con voto {voto}")
    else:
        # studente nuovo → aggiungi
        dizionario[nome] = voto
        print(f"Studente {nome} aggiunto con voto {voto}")
    return dizionario
print(add_student({"lorenzo":4}, "lorenzo", 10)) 
print(add_student({"lorenzo":4}, "marco", 10)) 

print("-------------------------------------------------------")

'''Accedi a un valore tramite chiave
Scrivi una funzione cerca_voto(diz, nome) che prende un dizionario {nome: voto} e un nome, e restituisce il voto corrispondente.
Se il nome non esiste, restituisci "Studente non trovato".'''
def cerca_voto(dizionario1:dict, nome:str):
    if nome in dizionario1:
        return dizionario1
    return "Studente non trovato"
print(cerca_voto({"marco":4}, "marco")) 
print(cerca_voto({"marco":4}, "lorenzo")) 

print("-------------------------------------------------------")

'''Modifica un valore
Scrivi una funzione aggiorna_voto(diz, nome, nuovo_voto) che aggiorna il voto di uno studente già presente nel dizionario.'''
def aggiorna_voto(dizionario3, nome:str, nuovo_voto:int) :
    if nome in dizionario3:
        dizionario3[nome] = nuovo_voto
    return f"voto aggiornato: {dizionario3}"
print(aggiorna_voto({"marco":4}, "marco", 7)) 

print("-------------------------------------------------------")

'''Rimuovi un elemento
Scrivi una funzione rimuovi_studente(diz, nome) che rimuove uno studente dal dizionario se esiste.
Se non esiste, restituisce un messaggio "Studente non trovato".'''
def rimuovi_studente(dizionario4:dict, nome:str):
    if nome in dizionario4:
        del dizionario4[nome]
        return dizionario4
    return "Studente non trovato..."
print(rimuovi_studente({"Marco": 5, "Lorenzo":8}, "Marco"))
print(rimuovi_studente({"Marco": 5, "Lorenzo":8}, "Luca"))

print("-------------------------------------------------------")

'''Trova lo studente con il voto più alto
Scrivi una funzione migliore(diz) che prende un dizionario {nome: voto} e restituisce il nome dello studente con il voto più alto.
Se ci sono più studenti con lo stesso voto massimo, scegli il primo trovato.'''
def migliore(dizionario: dict) -> str:
    # Inizializziamo il massimo con il primo studente
    massimo_nome = None
    massimo_voto = 0 

    for nome, voto in dizionario.items():
        if voto > massimo_voto:
            massimo_voto = voto
            massimo_nome = nome

    return f"{massimo_nome} ha il voto: {massimo_voto} piu alto"
print(migliore({"Marco": 5, "Lorenzo": 8, "Sara": 3}))