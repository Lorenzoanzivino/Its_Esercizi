'''Scrivi una funzione che prende una stringa di una o più parole e restituisce la stessa stringa, ma con tutte le parole che hanno cinque o più lettere invertite (proprio come il nome di questo Kata). Le corde passate sono costituite solo da lettere e spazi. Gli spazi saranno inclusi solo quando sarà presente più di una parola.'''

def spin_words(frase:str) -> str:
    parole = frase.split()    # divide la frase in parole
    parola_modificata = []


    for parola in parole:
        if len(parola) >= 5:
            parola_modificata.append(parola[::-1])    # inverte la parola
        else:
            parola_modificata.append(parola)

    return ' '.join(parola_modificata)
    
frase = "ciao sono Lorenzo"    # Output: ciao sono ozneroL
print(spin_words(frase))