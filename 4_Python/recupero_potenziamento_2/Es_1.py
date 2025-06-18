from typing import Self

class Frazione:
    __numeratore: int
    __denominatore: int

    # --- 8.A: costruttore, setter, getter, __str__, value ---
    def __init__(self, numeratore, denominatore) -> None:
        self.set_numeratore(numeratore)
        self.set_denominatore(denominatore)

    def get_numeratore(self) -> int:
        return self.__numeratore

    def set_numeratore(self, numeratore) -> None:
        if type(numeratore) != int or numeratore == 0:
            self.__numeratore = 13
        else:
            self.__numeratore = numeratore

    def get_denominatore(self) -> int:
        return self.__denominatore

    def set_denominatore(self, denominatore) -> None:
        if type(denominatore) != int or denominatore == 0:
            self.__denominatore = 5
        else:
            self.__denominatore = denominatore

    def __str__(self) -> str:
        return f"{self.__numeratore}/{self.__denominatore}"
    
    def __repr__(self) -> str:
        return f"{self.__numeratore}/{self.__denominatore}"

    def value(self) -> float:
        return round(self.__numeratore / self.__denominatore, 3)
    
    # --- 8.B: metodo MCD ---
    def mcd(self, x:int, y:int) -> int:
        divisore:int = 1
        
        if x > y:
            minimo:int = y
        else:
            minimo: int = x
        
        for i in range(2, minimo + 1):
            if x % i == 0 and y % i == 0:
                divisore = i
        return divisore
    
    # --- 8.C: semplifica frazioni ---
    def semplifica(self, lista_frazioni:list[Self]) -> list[Self]:
        l:list[Self] = []
        for frazione in lista_frazioni:
            if self.mcd(frazione.get_numeratore(), frazione.get_denominatore()) == 1:
                l.append(frazione)

            else:
                m_divisore:int = self.mcd(frazione.get_numeratore(), frazione.get_denominatore())
                num = frazione.get_numeratore() / m_divisore
                den = frazione.get_denominatore() / m_divisore
                l.append(Frazione(num, den))
            
        return l
    
     # --- 8.D: confronto frazioni originali vs semplificate ---
    def fractionCompare(self, l_originale: list[Self], l_semplificata: list[Self]) -> None:
        for i in range(len(l_originale)):
            val_orig = l_originale[i].value()
            val_sempl = l_semplificata[i].value()
            print(f"Valore frazione originale: {val_orig} --- Valore frazione ridotta: {val_sempl}")


# --- TEST SEPARATI PER OGNI PUNTO DELLA TRACCIA ---

# --- 8.A ---
print("\n--- PUNTO 8.A ---")
f1 = Frazione(10, 2)
print(f1)
print(f1.value())

f2 = Frazione(0, 0)  # diventa 13/5 per default
print(f2)
print(f2.value())

f3 = Frazione(4.5, 2)  # anche questo diventa 13/5
print(f3)
print(f3.value())

# --- 8.B ---
print("\n--- PUNTO 8.B ---")
print(f"MCD(12, 18) = {f1.mcd(12, 18)}")

# --- 8.C ---
print("\n--- PUNTO 8.C ---")
fra_list = [Frazione(1, 1), Frazione(12, 18), Frazione(5, 7), Frazione(2, 8)]
print("Frazioni originali:", fra_list)
print("Frazioni semplificate:", f1.semplifica(fra_list))

# --- 8.E ---
print("\n--- PUNTO 8.E ---")

l = [
    Frazione(2.5, 0),  # diventa 13/5
    Frazione(1, 2),
    Frazione(2, 4),
    Frazione(3, 5),
    Frazione(6, 9),
    Frazione(4, 7),
    Frazione(24, 36),
    Frazione(12, 36),
    Frazione(40, 60),
    Frazione(5, 11),
    Frazione(10, 45),
    Frazione(42, 78),
    Frazione(9, 15)
]

f = Frazione(1, 1)  # istanza per usare i metodi
l_s = f.semplifica(l)
f.fractionCompare(l, l_s)