'''5-10. Controllo dei nomi utente: procedi come segue per creare un programma che simula il modo in cui i siti Web assicurano che tutti abbiano un nome utente univoco.
• Crea un elenco di cinque o più nomi utente denominati current_users.
• Crea un altro elenco di cinque nomi utente denominati new_users. Assicurati che uno o due dei nuovi nomi utente siano anche nell'elenco current_users.
• Esegui un ciclo nell'elenco new_users per vedere se ogni nuovo nome utente è già stato utilizzato. In caso affermativo, stampa un messaggio che la persona dovrà immettere un nuovo nome utente. Se non è stato utilizzato un nome utente, stampa un messaggio che indica che il nome utente è disponibile.
• Assicurati che il tuo confronto non distingua tra maiuscole e minuscole. Se è stato utilizzato "John", "JOHN" non dovrebbe essere accettato. (Per fare ciò, dovrai creare una copia di current_users contenente le versioni minuscole di tutti gli utenti esistenti.)'''

current_users:list[str] = ["veronica", "stefano", "lorenzo", "marco", "luca"]

new_users:list[str] = ["carlo", "luca", "davide", "federico", "veronica"]

for nome in new_users:
    if nome in current_users:
        print(f"Il nome utente {nome} è gia stato utilizzato, metti un altro nome")
    else:
        print(f"Nome utente {nome} è disponibile")