'''5-9. Nessun utente: aggiungi un test if a hello_admin.py per assicurarti che l'elenco degli utenti non sia vuoto.
• Se l'elenco è vuoto, stampa il messaggio Dobbiamo trovare degli utenti!

• Rimuovi tutti i nomi utente dall'elenco e assicurati che venga stampato il messaggio corretto.'''


utente:list[str] = ["veronica", "stefano", "lorenzo", "marco", "admin", "antonio", "luca"]
if utente == []:
    print("Dobbiamo trovare degli utenti")
else:
    for nome in utente:
        if nome == "admin":
            print(f"Ciao Amministratore, vuole un rapportosullo stato?")
        else:
            print(f"Ciao {nome}, grazie per aver effettuato l'accesso.")


del utente[:]
if utente == []:
    print("Dobbiamo trovare degli utenti")
else:
    for nome in utente:
        if nome == "admin":
            print(f"Ciao Amministratore, vuole un rapportosullo stato?")
        else:
            print(f"Ciao {nome}, grazie per aver effettuato l'accesso.")