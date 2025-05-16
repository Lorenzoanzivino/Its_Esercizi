'''8-16. Importazioni: Utilizzando un programma che hai scritto che contiene una funzione, memorizza quella funzione in un file separato. Importa la funzione nel tuo file principale e chiama la funzione utilizzando ciascuno di questi approcci: importa nome_modulo da nome_modulo importa nome_funzione da nome_modulo importa nome_funzione come fn importa nome_modulo come mn da nome_modulo importa *'''

def function_name(nome:str):
    print(f"Ciao, {nome}! Come stai?")



# prova con un ciclo
messages:list[str] = ["messaggio_1", "messaggio_2", "messaggio_3", "messaggio_4", "messaggio_5", "messaggio_6"]

def show_messages(messages:str):
    print(messages)