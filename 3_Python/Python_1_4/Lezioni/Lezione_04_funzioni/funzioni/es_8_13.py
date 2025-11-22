'''8-13. Profilo utente: crea un profilo di te stesso chiamando build-profile(), utilizzando i tuoi cognomi e altri tre coppie di valori chiave che ti descrivono. Tutti i valori devono essere passati alla funzione come parametri. La funzione deve quindi restituire una stringa come "Corvo Eric, età 45, marrone capelli, peso 67"'''

def build_profile(cognome:str, nome:str, eta:int, colore_capelli:str, peso:int):
    # Crea una stringa con tutte le informazioni
    return f"Cognome: {cognome}, Nome: {nome}, età: {eta}, Capelli: {colore_capelli}, peso: {peso}\n"

# Chiamata alla funzione con i parametri
profilo = build_profile("Anzivino", "Lorenzo", 28, "marrone", 87)

# Stampa il profilo creato
print(profilo)


# secondo metodo
def build_profile2(nome, cognome, **user_info):
    stringa = f"nome: {nome}, cognome: {cognome}\n"
    for key, value in user_info.items():
        stringa += f" - {key}: {value}\n"

    return stringa

print(build_profile2("Lorenzo", "Anzivino", age = 28, city = "roma", job = "Cloud developer"))
