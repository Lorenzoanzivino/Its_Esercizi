# 1
'''Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.'''
def frequency_dict(elements: list) -> dict:
    dizionario:dict = {}
    for elemento in elements:
        if elemento not in dizionario:
            dizionario[elemento] = 1
        else:
            dizionario[elemento] += 1
    return dizionario
print(frequency_dict(['mela', 'banana', 'mela']))

# 2
'''Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, ma scontati del 10%'''
def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    dizionario_nuovo:dict[str:float] = {}

    for prodotto, prezzo in prodotti.items():
        if prodotto not in dizionario_nuovo:
            if prezzo > 20:
                dizionario_nuovo[prodotto] = prezzo * 0.9
    return dizionario_nuovo
print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0}))

# 3
'''Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.'''
def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    dizionario2:dict[str:list[int]] = {}
    for tupla in tuples:
        chiave = tupla[0]
        valore = tupla[1]
        if chiave not in dizionario2:
            dizionario2[chiave] = [valore]
        else:
            dizionario2[chiave].append(valore)
    return dizionario2
print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))
print(lista_a_dizionario([]))

# 4
'''Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo). L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo. La funzione ritorna "Accesso consentito" oppure "Accesso negato".''' 
def check_access(username: str, password:'12345', is_active: bool) -> str:
    if username == 'admin' and password == '12345' and is_active == True:
        return 'Accesso consentito'
    return 'Accesso negato'
print(check_access("admin", "12345", True)) #Accesso consentito
print(check_access("admin", "54321", True)) #Accesso negato

# 5
'''Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.'''
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    dict3 = {}
    for chiave, valore in dict1.items():
        if chiave in dict2:
            dict3[chiave] = valore + dict2[chiave]
        else:
            dict3[chiave] = valore
    for chiave, valore in dict2.items():
        if chiave not in dict3:
            dict3[chiave] = valore
    return dict3
print(merge_dictionaries({'x': 5}, {'x': -5})) #{'x': 0}

# 6
'''Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 1, 2, 3, 4, 5, 6, 7
b) 3, 8, 13, 18, 23
c) 20, 14, 8, 2, -4, -10
d) 19, 27, 35, 43, 51'''
def print_seq(): 
    print("Sequenza a):")
    for i in range(1, 8):
        print(i)
    print('\n')
    print("Sequenza b):")
    for i2 in range(3, 24, 5):
        print(i2)
    print('\n')
    print("Sequenza c):")
    for i3 in range(20, -11, -6):
        print(i3)
    print('\n')
    print("Sequenza d):")
    for i4 in range(19, 52, 8):
        print(i4)
    print('\n')
    return
print_seq()

# 9
'''
Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere. La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.'''
def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA == True or (conditionB == True and conditionC == True):
        return "Operazione permessa"
    return "Operazione negata"
print(check_combination(True, False, True))# Operazione permessa
print(check_combination(False, True, False)) # Operazione negata

# 11
'''Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.'''
def sum_above_threshold(numbers: list[int], threshold:int) -> int:
    somma = 0
    for numeri in numbers:
        if numeri > threshold:
            somma += numeri
    return somma
print(sum_above_threshold([15, 5, 25], 20)) # 25

# 13
'''
Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
- se x è pari, deve essere diviso per 2;
- se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.'''
def transform(x: int) -> int:
    if x % 2 == 0:
        return x / 2
    return (x * 3) -1 

print(transform(4)) # 2
print(transform(-10)) # -5

# 14
'''
Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.'''
def classifica_numeri(lista: int) -> dict[str:list[int]]:
    dict4 = {'pari': [], 'dispari': []}
    for numero in lista:
        if numero % 2 == 0:
            dict4['pari'].append(numero)
        else:
            dict4['dispari'].append(numero)
    return dict4

print(classifica_numeri([1, 2, 3, 4, 5, 6])) # {'pari': [2, 4, 6], 'dispari': [1, 3, 5]}
print(classifica_numeri([])) # {'pari': [], 'dispari': []}

# 15
'''
Scrivi una funzione che prenda un dizionario e un valore, e ritorni la prima chiave che corrisponde a quel valore, o None se il valore non è presente.'''
def trova_chiave_per_valore(dizionario: dict[str, int], valore: int) -> str | None:
    for chiave, val in dizionario.items():
        if val == valore:
            return chiave
    return None

print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200)) # b
print(trova_chiave_per_valore({'k1': 'v1', 'k2': 'v2'}, 'v3')) # None