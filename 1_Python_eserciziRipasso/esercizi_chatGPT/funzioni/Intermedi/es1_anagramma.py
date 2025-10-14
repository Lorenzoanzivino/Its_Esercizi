'''4. Anagramma

Scrivi una funzione che prende due stringhe e dice se sono anagrammi (cioè contengono le stesse lettere, ma in ordine diverso).

# Esempio: "roma" e "amor" → True'''

stringa_1 = "amor"
stringa_2 = "roma"

def anagrammi(stringa_1:str, stringa_2:str) -> bool:
    if len(stringa_1) != len(stringa_2):
        return False
    
    lista_2:list = list(stringa_2)

    for char in stringa_1:
        if char in lista_2:
            lista_2.remove(char)
        else:
            return False  # carattere non trovato

    return True  # tutti i caratteri trovati

# Test
print(anagrammi("roma", "amor"))  # → True
print(anagrammi("roma", "amore")) # → False
print(anagrammi("test", "sett"))  # → True

