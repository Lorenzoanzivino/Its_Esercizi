'''In biologia molecolare, le molecole di DNA possono essere viste come stringhe sull’alfabeto dei nucleotidi
A = adenina, C = citosina, G =guanina, T = timina.

Ad esempio: DNA: CAGCTGATCGATGCTAGCCTG.'''

import re

def isDNA(seq: str) -> bool:
    pattern = r"^[ACGT]+$"

    if re.fullmatch(pattern, seq.upper()):
        return True
    else:
        return False

def sovrapposizione_dna(s1:str, s2:str) -> str:
    if isDNA(s1) and isDNA(s2):
        nuova_stringa:str = ""
        
        count:int = 0
        for char in s1:
            if char == s2[count]:
                count += 1

                nuova_stringa += char

            elif char == s2[0]:
                count = 1

                nuova_stringa = char

            else:
                count = 0

                nuova_stringa = ""
        
        if count > 0:
            return nuova_stringa
        else:
            return "Error!"
            
print(sovrapposizione_dna("GGTACCGTGA", "CGTGAACCTT"))

print(sovrapposizione_dna("AGCTTACG", "ACGTTCGA"))