'''Esercizio 8.

Si scriva una funzione ricorsiva vowelsCounter che conti il numero di vocali in una stringa.

Suggerimento: ogni volta che si effettua una chiamata ricorsiva, si utilizzi lo slicing per ottenere una nuova stringa formata dai caratteri compresi tra il secondo e l'ultimo della stringa originale.
L'ultima chiamata ricorsiva avverrà quando la stringa non contiene caratteri.'''

def vowelsCounter(s: str) -> int:
    if not s:
        return 0
    elif s[0].lower() in ["a", "e", "i", "o", "u"]:
        return 1 + vowelsCounter(s[1:])
    else:
        return vowelsCounter(s[1:])

print(f"La stringa \"\" contiene {vowelsCounter('')} vocali")
print(f"La stringa \"ciao\" contiene {vowelsCounter('ciao')} vocali")
print(f"La stringa \"Pappagallo\" contiene {vowelsCounter('Pappagallo')} vocali")
