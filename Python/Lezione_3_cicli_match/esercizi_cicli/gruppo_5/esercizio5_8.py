'''5-8. Ciao amministratore: crea un elenco di cinque o più nomi utente, incluso il nome "admin". Immagina di scrivere codice che stamperà un saluto a ogni utente dopo che avrà effettuato l'accesso a un sito web. Scorri l'elenco e stampa un saluto a ogni utente.
• Se il nome utente è "admin", stampa un saluto speciale, come Ciao amministratore, vuoi vedere un rapporto sullo stato?
• Altrimenti, stampa un saluto generico, come Ciao Jaden, grazie per aver effettuato di nuovo l'accesso.'''

utente:list[str] = ["veronica", "stefano", "lorenzo", "marco", "admin", "antonio", "luca"]

for nome in utente:
    if nome == "admin":
        print(f"Ciao Amministratore, vuole un rapportosullo stato?")
    else:
        print(f"Ciao {nome}, grazie per aver effettuato l'accesso.")