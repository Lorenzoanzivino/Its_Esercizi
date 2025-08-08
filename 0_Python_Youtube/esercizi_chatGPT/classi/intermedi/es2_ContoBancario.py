'''
🏦 Esercizio 2 – Conto Bancario

Crea una classe ContoBancario con:

    attributi privati: __, __saldo

    metodo deposita(importo)

    metodo preleva(importo): solo se c'è abbastanza saldo

    metodo mostra_saldo()

    proprietà saldo (con @property) per leggere il saldo in modo sicuro

Test: crea un conto, fai alcuni versamenti e prelievi, mostra il saldo.'''

class ContoBancario:
    __titolare:str
    __saldo:float

    def __init__(self, titolare:str, saldo:float) -> None:

        if saldo < 0:
            raise ValueError("il saldo non può scendere sotto zero")
        self.__titolare = titolare
        self.__saldo = saldo

    def get_titolare(self) -> str:
        return self.__titolare
    
    def get_saldo(self) -> str:
        return self.__saldo

    def deposita(self, importo:float) -> float:
        self.__saldo += importo
        return self.__saldo
    
    def preleva(self, importo:float) -> float:
        if self.__saldo < importo:
            raise ValueError("Non puoi prelevare questa somma")
        self.__saldo -= importo
        
    def mostra_saldo(self) -> str:
        return f"Il tuo saldo ammonta a: {self.get_saldo()}€"
    
if __name__ == "__main__":

    conto = ContoBancario("Lorenzo Anzivino", 100)
    conto.deposita(100)
    conto.preleva(50)
    conto.preleva(100)
    conto.preleva(50)

    print(conto.mostra_saldo())

    conto.preleva(15)
    print(conto.mostra_saldo())




