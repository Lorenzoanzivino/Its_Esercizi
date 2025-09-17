'''Scrivere una funzione check_length(), che prende una stringa come argomento.
Usando if / else, controlla se la lunghezza della stringa è maggiore, più piccola o uguale a 10 caratteri'''

text:str = input("Inserisci una stringa: ")

def check_lenght(text):
    if len(text) < 10:
        print("La stringa è più piccola di 10 caratteri")
    elif len(text) == 10:
        print("La stringa è uguale a 10 caratteri")
    else:
        print("La stringa è più grande di 10 caratteri")

# Non metto il PRINT perche non ho il return
check_lenght(text)