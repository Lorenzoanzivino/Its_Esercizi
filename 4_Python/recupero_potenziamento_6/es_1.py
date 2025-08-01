'''Prima di scivere la funzione in Python, è obbligatorio produrre uno schema che rappresenti ricorsivamente quanto richiesto. Dopo aver prodotto lo schema, procedere con l'implementazione solo quando indicato dal docente.
 
Un palindromo è una stringa che non cambia anche se letta al contrario, come la stringa "radar". Si scriva una funzione ricorsiva chiamata recursivePalindrome() che accetti in input un parametro di tipo stringa e restituisca True se l'argomento è un palindromo e False altrimenti.

Non si tenga conto degli spazi nella stringa e non si faccia distinzione tra lettere maiuscole e minuscole.

La funzione dovrebbe considerare palindrome le seguenti stringhe:
"radar"
"Anna"
" I topi non avevano nipoti"

La funzione non dovrebbe considerare palindrome le seguenti stringhe:
"casa"
"Marta"
"Roma e Amore"

Suggerimento: usare la funzione replace() per sostituire gli spazi con una stringa vuota.'''

def recursivePalindrome(stringa:str) -> bool:

    stringa = stringa.replace(" ", "").lower()

    if len(stringa) == 0:
        return True
    
    if stringa[0] != stringa[-1]:
        return False
    
    return recursivePalindrome(stringa[1:-1])


print(recursivePalindrome("radar"))
print(recursivePalindrome("Anna"))
print(recursivePalindrome("i topi non avevano nipoti"))

print(recursivePalindrome("casa"))
print(recursivePalindrome("Marta"))
print(recursivePalindrome("Roma e Amore"))