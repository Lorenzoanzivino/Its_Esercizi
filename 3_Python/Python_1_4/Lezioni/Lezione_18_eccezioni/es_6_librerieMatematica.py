'''es 6.Libreria Matematica Personalizzata

Crea una libreria Python per gestire frazioni, con gestione integrata degli errori. Deve includere funzioni per:

    Creare una frazione da numeratore e denominatore

    Ottenere numeratore e denominatore di una frazione

    Semplificare una frazione

    Sommare, sottrarre, moltiplicare e dividere frazioni

    Verificare se due frazioni sono equivalenti

Tutte le funzioni devono usare try-except per gestire errori come:

    Denominatore nullo

    Operazioni non supportate

    Divisione per zero

La libreria deve sollevare eccezioni personalizzate per indicare errori specifici.'''


import math

# Eccezioni personalizzate
class DenominatoreZeroError(Exception):
    pass

class OperazioneNonSupportataError(Exception):
    pass

class DivisionePerZeroError(Exception):
    pass

class Frazione:
    def __init__(self, numeratore, denominatore):
        try:
            if denominatore == 0:
                raise DenominatoreZeroError("Il denominatore non può essere zero.")
            self.numeratore = int(numeratore)
            self.denominatore = int(denominatore)
            self.simplify()
        except ValueError:
            raise ValueError("Numeratore e denominatore devono essere numeri interi.")
    
    def simplify(self):
        gcd = math.gcd(self.numeratore, self.denominatore)
        self.numeratore //= gcd
        self.denominatore //= gcd
        # Mantieni il denominatore positivo
        if self.denominatore < 0:
            self.denominatore *= -1
            self.numeratore *= -1
    
    def get_numeratore(self):
        return self.numeratore
    
    def get_denominatore(self):
        return self.denominatore
    
    def __str__(self):
        return f"{self.numeratore}/{self.denominatore}"
    
    def __eq__(self, other):
        if not isinstance(other, Frazione):
            return False
        return (self.numeratore == other.numeratore and 
                self.denominatore == other.denominatore)
    
    def somma(self, other):
        if not isinstance(other, Frazione):
            raise OperazioneNonSupportataError("Somma supportata solo tra frazioni.")
        num = self.numeratore * other.denominatore + other.numeratore * self.denominatore
        den = self.denominatore * other.denominatore
        return Frazione(num, den)
    
    def sottrai(self, other):
        if not isinstance(other, Frazione):
            raise OperazioneNonSupportataError("Sottrazione supportata solo tra frazioni.")
        num = self.numeratore * other.denominatore - other.numeratore * self.denominatore
        den = self.denominatore * other.denominatore
        return Frazione(num, den)
    
    def moltiplica(self, other):
        if not isinstance(other, Frazione):
            raise OperazioneNonSupportataError("Moltiplicazione supportata solo tra frazioni.")
        num = self.numeratore * other.numeratore
        den = self.denominatore * other.denominatore
        return Frazione(num, den)
    
    def dividi(self, other):
        if not isinstance(other, Frazione):
            raise OperazioneNonSupportataError("Divisione supportata solo tra frazioni.")
        if other.numeratore == 0:
            raise DivisionePerZeroError("Divisione per frazione zero non permessa.")
        num = self.numeratore * other.denominatore
        den = self.denominatore * other.numeratore
        return Frazione(num, den)
    
    def equivalente(self, other):
        if not isinstance(other, Frazione):
            return False
        return self == other

# Esempio di utilizzo
try:
    f1 = Frazione(2, 4)
    f2 = Frazione(1, 2)
    print("Frazione 1:", f1)
    print("Frazione 2:", f2)
    print("Somma:", f1.somma(f2))
    print("Sottrazione:", f1.sottrai(f2))
    print("Moltiplicazione:", f1.moltiplica(f2))
    print("Divisione:", f1.dividi(f2))
    print("Sono equivalenti?", f1.equivalente(f2))
except (DenominatoreZeroError, OperazioneNonSupportataError, DivisionePerZeroError, ValueError) as e:
    print("Errore:", e)
