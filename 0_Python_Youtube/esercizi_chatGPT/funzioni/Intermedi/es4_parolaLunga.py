'''4. Parola più lunga

Scrivi una funzione che prende una frase e restituisce la parola più lunga contenuta nella frase.

# Input: "Il gatto corre nel giardino"
# Output: "giardino"

Suggerimento: usa .split() per dividere la frase.'''


def parola_piu_lunga(frase:str) -> str:
    parola_lunga:str = ""
    for parola in frase.split():
        if len(parola) >= len(parola_lunga):
            parola_lunga = parola
    
    return parola_lunga

# Test
frase = "Il gatto corre nel giardino"
print(parola_piu_lunga(frase))  # Output: "giardino"