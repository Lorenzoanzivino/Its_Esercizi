'''Es_Mostri_contro_Alieni / Recupero_Potenzamento_3'''

import random

class Creatura:
    def __init__(self, nome:str) -> None:
        self.set_nome(nome)    # Attributo privato con __ diverramente dopo il self.

    def get_nome(self) -> str:
        return self.__nome
    
    def set_nome(self, nome: str) -> None:
        if isinstance(nome, str):
            self.__nome = nome
        else:
            self.__nome = "Creatura Generica"
    
    def __str__(self):
        return f"Creatura: {self.__nome}"
    
class Alieno(Creatura):
    def __init__(self, nome:str = "") -> None:
        self.__set_matricola()
        nome_nuovo:str = f"Robot-{self.__matricola}"

        if nome != nome_nuovo:
            nome = nome_nuovo
        else:
            print("Attenzione! Tutti gli Alieni devono avere il nome 'Robot' seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")

        super().__init__(nome)
        self.__set_munizioni()

    def get_matricola(self) -> int:
        return self.__matricola
    
    def get_munizioni(self) -> list[int]:
        return self.__munizioni
    
    def __set_matricola(self) -> None:
        self.__matricola = random.randint(10000, 90000)

    def __set_munizioni(self) -> None:
        self.__munizioni = [i**2 for i in range(15)]    # Non servono controlli perche la lista la sto creando io

    def __str__(self):
        return f"Alieno: {self.get_nome()}"
    
class Mostro(Creatura):
    def __init__(self, nome, urlo_vittoria:str, gemito_sconfitta:str) -> None:
        super().__init__(nome)
        self.__set_vittoria(urlo_vittoria)
        self.__set_sconfitta(gemito_sconfitta)
        self.__set_assalto()

    def get_urlo_vittoria(self) -> str:
        return self.__urlo_vittoria
    
    def __set_vittoria(self, vittoria: str) -> None:
        if isinstance(vittoria, str) and vittoria.strip():    # Rimuove spazi all'inizio e alla fine
            self.__urlo_vittoria = vittoria
        else:
            self.__urlo_vittoria = "GRAAAHHH"

    def get_gemito_sconfitta(self) -> str:
        return self.__gemito_sconfitta
    
    def get_assalto(self) -> list[int]:
        return self.__assalto

    def __set_sconfitta(self, sconfitta: str) -> None:
        if isinstance(sconfitta, str) and sconfitta.strip():    # Rimuove spazi all'inizio e alla fine
            self.__gemito_sconfitta = sconfitta
        else:
            self.__gemito_sconfitta = "Uuurghhh"

    def __set_assalto(self) -> None:
        self.__assalto:list[int] = []
        while len(self.__assalto) < 15:
            numero = random.randint(1, 100)
            if numero not in self.__assalto:
                self.__assalto.append(numero)

    def __str__(self):
        nome = self.get_nome()
        alternanza:str = ""
        i = 0
        for char in nome:
            if i % 2 == 0:    # Se è pari
                alternanza += char.lower()
            else:
                alternanza += char.upper()
            i += 1
        return f"Mostro: {alternanza}"
    
def pariUguali(a: list[int], b: list[int]) -> list[int]:
    __c:list[int] = []

    for i in range(len(a)):
        if a[i] % 2 == 0 and b[i] % 2 == 0:
            __c.append(1)
        else:
            __c.append(0)

    return __c