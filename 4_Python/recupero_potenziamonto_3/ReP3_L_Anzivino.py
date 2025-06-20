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
    
#===============================================================================================

class Alieno(Creatura):
    def __init__(self, nome:str = "") -> None:
        self.__set_matricola()
        nome_nuovo:str = f"Robot-{self.__matricola}"

        if nome != "" and nome != nome_nuovo:
            print("Attenzione! Tutti gli Alieni devono avere il nome 'Robot' seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")
            nome = nome_nuovo

        elif nome == "":
            nome = nome_nuovo

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
    c:list[int] = []

    if len(a) != len(b):
        raise ValueError("Le due liste devono avere la stessa lunghezza")
    else:
        for i in range(len(a)):
            if a[i] % 2 == 0 and b[i] % 2 == 0:
                c.append(1)
            else:
                c.append(0)

        return c
    
def combattimento(a:Alieno, m:Mostro) -> None|str:

    if not isinstance(a, Alieno) or not isinstance(m, Mostro):
        print("Errore: uno o entrambi gli oggetti non sono validi per il combattimento.")
        return None

    risultati: list[int] = pariUguali(a.get_munizioni(), m.get_assalto())

    pari:int = risultati.count(1)
    
    if pari > 4:
        for i in range(3):
            print(m.get_urlo_vittoria())
        return m
    else:
        print(f"L'alieno {a.get_nome()} ha vinto! Il mostro {m.get_nome()} ha perso!")
        print(m.get_gemito_sconfitta())
        return a

def proclamaVincitore(c: Creatura) -> None:
    print("\nCombattimento\n")

    for _ in range(3):
        print(c.verso_vittoria)

    if isinstance(c, Mostro):
        print("\nI Mostri hanno vinto!\n")
    elif isinstance(c, Alieno):
        print("\nGli Alieni hanno vinto!\n")
    else:
        print("Nessun vincitore valido.")
        return

    testo = str(c)
    larghezza = len(testo) + 10
    altezza = 5

    for i in range(altezza):
        if i == 0 or i == altezza - 1:
            print("*" * larghezza)
        elif i == 2:
            spaziInterni = larghezza - 2
            spaziPrima = (spaziInterni - len(testo)) // 2
            spaziDopo = spaziInterni - len(testo) - spaziPrima
            print("*" + " " * spaziPrima + testo + " " * spaziDopo + "*")
        else:
            print("*" + " " * (larghezza - 2) + "*")


def main():
    # Per test deterministico, forziamo la matricola e le munizioni
    a = Alieno()
    a._Alieno__matricola = 41119  # Imposta matricola specifica
    a.set_nome(f"Robot-{a.get_matricola()}")
    a._Alieno__munizioni = [i**2 for i in range(15)]  # Munizioni fisse
    print(a)
    print("Munizioni:", a.get_munizioni())
    print()  # Riga vuota

    # Per test deterministico, forziamo l’assalto del mostro
    m = Mostro("Gorthor", "GRAAAHHH", "Uuurghhh")
    m._Mostro__assalto = [13, 23, 28, 80, 50, 56, 33, 55, 15, 20, 15, 94, 42, 16, 46]
    print(m)
    print("Assalto:", m.get_assalto())
    print()  # Riga vuota

    print("Combattimento\n")

    # Eseguiamo il combattimento ma NON stampiamo il messaggio interno
    risultati: list[int] = pariUguali(a.get_munizioni(), m.get_assalto())
    pari:int = risultati.count(1)

    if pari > 4:
        # Mostro vince
        for _ in range(3):
            print(m.get_urlo_vittoria())
        vincitore = m
    else:
        # Alieno vince
        vincitore = a

    print()  # Riga vuota

    # Stampa proclama vincitore e rettangolo
    proclamaVincitore(vincitore)

if __name__ == "__main__":
    main()