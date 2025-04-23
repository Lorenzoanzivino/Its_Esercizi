'''
Esercizio 3C-5. Scrivere un programma in Python che memorizzi il nome, il ruolo e l'età di un utente in un dizionario. Il nome, il ruolo e l'età devono essere inseriti in input dall'utente stesso. Il programma deve determinare il livello di accesso ai servizi in base al ruolo e all'età dell'utente secondo questo schema:

- Admin → "Accesso completo a tutte le funzionalità."
- Moderatore → "Può gestire i contenuti ma non modificare le impostazioni."
- Utente adulto (età ≥ 18) → "Accesso standard a tutti i servizi."
- Utente minorenne (età < 18) → "Accesso limitato! Alcune funzionalità sono bloccate."
- Ospite → "Accesso ristretto! Solo visualizzazione dei contenuti."
- Ruolo non riconosciuto → "Attenzione! Ruolo non riconsciuto! Accesso Negato!"

Expected Output:

Digitare nome dell'utente: Mario Rossi
Digitare ruolo dell'utente: admin
Digitare l'età dell'utente: 30
Output: Accesso completo a tutte le funzionalità.

- - - - - - - - - - - - - - - - - - - - - - - - - - -

Digitare nome dell'utente: Giulia Bianchi
Digitare ruolo dell'utente: utente
Digitare l'età dell'utente: 16
Output: Accesso limitato! Alcune funzionalità sono limitate!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digitare nome dell'utente: Sara Neri
Digitare ruolo dell'utente: vip
Digitare l'età dell'utente: 22
Output: Attenzione! Ruolo non riconosciuto! Accesso Negato!

 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digitare nome dell'utente: Luca Verdi
Digitare ruolo dell'utente: moderatore
Digitare l'età dell'utente: 25
Output: Salve Luca Verdi! Può gestire i contenuti ma non modificare le impostazioni.
'''
#variabili in input
nome:str = input("Inserire il tuo Nome e cognome: ")
ruolo:str = input("Inserisci il tuo ruolo: admin, moderatore, utente, ospite: ")
anni:int = int(input("Inserisci i tuoi anni: "))

#dizionario con valore dell'input
user:dict[any] = {"nome":nome, "ruolo":ruolo, "anni":anni}

match user:
    case {"nome":nome,"ruolo":"admin", "anni":anni}:
        print("Accesso completo a tutte le funzionalità.")
    case {"nome":nome,"ruolo":"moderatore", "anni":anni}:
        print(f"Salve {nome}! può gestire i contenuti ma non modificare le impostazioni.")
    case {"nome":nome,"ruolo":"utente", "anni":anni}:
        if anni >= 18:
            print("Accesso standard a tutti i servizi.")
        else:
            print("Accesso limitato! Alcune funzionalità sono bloccate.")
    case {"nome":nome,"ruolo":"ospite", "anni":anni}:
        print("Accesso ristretto! Solo visualizzazione dei contenuti.")
    case _:
        print("Attenzione! Ruolo non riconosciuto! Accesso Negato!")
        
    
    
