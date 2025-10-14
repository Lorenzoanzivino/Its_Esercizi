'''3. Palindromo ignorando spazi e maiuscole

Scrivi una funzione che controlla se una frase è un palindromo, ignorando spazi e differenze tra maiuscole/minuscole.

# Input: "i topi non avevano nipoti"
# Output: True'''

def palindromo(frase: str) -> bool:
    print(f"Frase originale: {frase}")
    
    # 1. Rimuovi gli spazi
    senza_spazi = frase.replace(" ", "")
    print(f"Senza spazi: {senza_spazi}")
    
    # 2. Rendi tutto minuscolo
    pulita = senza_spazi.lower()
    print(f"Minuscola e pulita: {pulita}")
    
    # 3. Crea la versione invertita
    invertita = pulita[::-1]
    print(f"Invertita: {invertita}")
    
    # 4. Confronta
    risultato = pulita == invertita
    print(f"È palindromo? {risultato}")
    
    return risultato

# Test
frase = "i topi non avevano nipoti"
palindromo(frase)