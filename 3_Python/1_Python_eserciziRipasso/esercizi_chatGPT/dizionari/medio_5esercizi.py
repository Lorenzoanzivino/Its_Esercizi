'''1. Conta lettere in una parola
Scrivi una funzione conta_lettere(parola) che prende una stringa e restituisce un dizionario con il conteggio di ogni lettera.
Esempio: "casa" → {'c': 1, 'a': 2, 's': 1}.'''
def conta_lettere(parola:str) -> dict:
    diz:dict={}
    for char in parola:
        if char not in diz:
            diz[char] = 1
        else:
            diz[char] += 1
    return diz
print(conta_lettere("casa"))

'''2. Media voti studenti
Hai un dizionario {nome: [voti]} dove i voti sono liste di numeri.
Scrivi una funzione media_voti(diz) che restituisce un nuovo dizionario {nome: media} con la media dei voti di ogni studente.'''
def media_voti(diz2:dict[str, list[int]]) -> dict:
    nuovo_diz:dict = {}
    for nome in diz2:
        if nome in diz2:
            voti = diz2[nome]
            somma = sum(voti)
            media = somma / len(voti)
            nuovo_diz[nome]= media

    return nuovo_diz
print(media_voti({"lorenzo":[8, 9, 10]}))


'''3. Filtra numeri positivi - LIST COMPREHENSION
Scrivi una funzione filtra_positivi(lista) che prende una lista di numeri e restituisce una nuova lista contenente solo i numeri positivi.
Prova a farlo sia con un ciclo for sia con list comprehension.'''
def filtra_positivi(lista:list) -> list:
    return [n for n in lista if n > 0 ]
print(filtra_positivi([-1,-3,-4,-1,3,4,5]))


'''3. Filtra numeri positivi - FOR
Scrivi una funzione filtra_positivi(lista) che prende una lista di numeri e restituisce una nuova lista contenente solo i numeri positivi.
Prova a farlo sia con un ciclo for sia con list comprehension.'''
def filtra_positivi(lista:list) -> list:
    lista_positivi:list = []
    for n in lista:
        if n > 0:
            lista_positivi.append(n)
    return lista_positivi
print(filtra_positivi([-1,-3,-4,-1,3,4,5]))


'''4. Inversione dizionario
Scrivi una funzione inverti_dizionario(diz) che prende un dizionario {chiave: valore} e restituisce un nuovo dizionario {valore: chiave}.
Assumi che i valori siano unici, quindi non ci saranno conflitti.'''


'''5. Rimuovi duplicati da lista di dizionari
Hai una lista di dizionari, ad esempio: 
persone = [
    {"nome": "Lorenzo", "eta": 25},
    {"nome": "Anna", "eta": 30},
    {"nome": "Lorenzo", "eta": 25},
    {"nome": "Marco", "eta": 22}
]
Scrivi una funzione rimuovi_duplicati(lista) che prende una lista di dizionari e restituisce una nuova lista contenente gli stessi dizionari ma senza duplicati.
Due dizionari sono considerati duplicati se hanno le stesse coppie chiave-valore.'''

def rimuovi_duplicati(lista:list) -> list[dict]:
    lista_nuova = []
    for dizionario in lista:
        if dizionario not in lista_nuova:
            lista_nuova.append(dizionario)
    return lista_nuova

print(rimuovi_duplicati(lista = [
    {"nome": "Lorenzo", "eta": 25},
    {"nome": "Anna", "eta": 30},
    {"nome": "Lorenzo", "eta": 25},
    {"nome": "Marco", "eta": 22}
]))
