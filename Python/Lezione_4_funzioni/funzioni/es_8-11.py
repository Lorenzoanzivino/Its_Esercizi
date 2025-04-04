'''8-11. Messaggi archiviati: Inizia con il tuo lavoro dall'esercizio 8-10. Chiamare la funzione send-messages() con una copia dell'elenco dei messaggi. Dopo aver chiamato la funzione, stampare entrambe le tue liste per mostrare che l'elenco originale ha mantenuto i suoi messaggi.'''


messages:list[str] = ["messaggio_1", "messaggio_2", "messaggio_3", "messaggio_4", "messaggio_5", "messaggio_6"]

def show_messages(messages):
    for i in messages:
        print(f"Messaggio: {i}")

# Funzione per inviare i messaggi
def send_messages(messages):
    # Lista dove spostare i messaggi inviati
    sent_messages = []  
    while messages:
        sms = messages.pop(0)  # Sposta il messaggio nella lista 'sent_messages'
        print(f"Inviando: {sms}")
        sent_messages.append(sms)  # Aggiungi il messaggio alla lista 'sent_messages'
    
    return sent_messages

# Mostra i messaggi prima dell'invio
print("Messaggi prima dell'invio:")
show_messages(messages)

# Invia i messaggi e ottieni la lista dei messaggi inviati
sent_messages = send_messages(messages[:])

# Mostra i messaggi inviati e quelli rimasti
print("\nMessaggi inviati:")
show_messages(sent_messages)
print("\nMessaggi rimasti:")

# La lista 'messages' dovrebbe essere vuota
show_messages(messages)  