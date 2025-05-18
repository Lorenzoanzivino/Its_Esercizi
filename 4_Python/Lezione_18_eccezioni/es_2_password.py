'''es 2.Validazione della Password

Scrivi una funzione validate_password(password) che verifichi se una password soddisfa determinati criteri:

    Lunghezza minima di 20 caratteri

    Almeno tre lettere maiuscole

    Almeno quattro caratteri speciali

Se la password non è valida, solleva un'eccezione personalizzata (ad esempio, InvalidPasswordError).'''


import string

# Definizione dell'eccezione personalizzata
class InvalidPasswordError(Exception):
    pass

maiuscole:list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

caratteri = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '{', '|', '}', '~', '¬', '§', '±', '©', '®', '™', '€']

password:list=[]

def validate_password(password:str):
    # 1. Verifica lunghezza minima di 20 caratteri
    if len(password) < 20:
        raise InvalidPasswordError("La password deve contenere almeno 20 caratteri.")
    
    # 2. Verifica almeno 3 lettere maiuscole
    for lettera in maiuscole:
        if lettera == maiuscole:  # Controlla se è una lettera maiuscola
            password.append(lettera)
        if lettera in password == 3:
            break
    
    if lettera in password < 3:
        raise InvalidPasswordError("La password deve contenere almeno 3 lettere maiuscole.")
    
    # 3. Verifica almeno 4 caratteri speciali
    special_count = 0
    for c in password:
        if c in string.punctuation:  # Controlla se è un carattere speciale
            special_count += 1
    
    if special_count < 4:
        raise InvalidPasswordError("La password deve contenere almeno 4 caratteri speciali.")

# Esempio di utilizzo
try:
    validate_password("Ab1!Abc$@defghijKlmn#@")
except InvalidPasswordError as e:
    print(e)
