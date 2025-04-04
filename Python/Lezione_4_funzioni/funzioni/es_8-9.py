'''8-9. Messaggi: Fare un elenco contenente una serie di brevi messaggi di testo. Passare l'elenco a una funzione chiamata show-messages(), che stampa ogni messaggio di testo.'''

messages:list[str] = ["messaggio_1", "messaggio_2", "messaggio_3", "messaggio_4", "messaggio_5"]

def show_messages(messages) -> None:
    '''
    commentare sempre le funzioni
    '''
    for i in messages:
        print(f"Messaggio: {i}")

show_messages(messages)