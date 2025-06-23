'''Es_Mostri_contro_Alieni / Recupero_Potenzamento_3'''

import random

class Creatura:

    _nome: str

    def __init__(self, nome: str) -> None:
        self.setNome(nome)

    def setNome(self, nome: str) -> None:
        if nome:
            self._nome = nome
        else:
            self._nome = 'Creatura Generica'

    def get_nome(self) -> str:
        return self._nome
    
    def __str__(self) -> str:
        return f'Creatura: {self.get_nome()}'
    
#===============================================================================================

class Alieno(Creatura): 

    _matricola: int # Intero >= 0
    _munizioni: list[int]

    def __init__(self, nome: str):
        super().__init__(nome)
        self._setMatricola()
        self._setMunizioni()
        if self._nome != 'Robot' or not(10000 <= self.matricola() <= 90000):
            print('Attenzione! Tutti gli Alieni devono avere il nome "Robot" seguito dal numero di matricola! '
                  'Reimpostazione nome Alieno in Corso!')
            self._nome = f'Robot-{self.matricola()}'
        else:
            self._nome = nome.title() + f'-{self.matricola()}'

    def _setMatricola(self) -> None:
        self._matricola = random.randint(10000, 90000)

    def _setMunizioni(self) -> None:
        self._munizioni = [n**2 for n in range(15)]

    def matricola(self) -> int:
        return self._matricola
    
    def munizioni(self) -> list[int]:
        return self._munizioni
    
    def __str__(self):
        return super().__str__()
    
#===============================================================================================
    
class Mostro(Creatura):

    _urlo_vittoria: str
    _gemito_sconfitta: str
    _assalto: list[int]

    def __init__(self, nome, urlo_vittoria:str = "GRAAAHHH", gemito_sconfitta:str="Uuurghhh") -> None:
        super().__init__(nome)
        self.__set_vittoria(urlo_vittoria)
        self.__set_sconfitta(gemito_sconfitta)
        self.__set_assalto()

    def get_urlo_vittoria(self) -> str:
        return self.__urlo_vittoria
                
    def get_gemito_sconfitta(self) -> str:
        return self.__gemito_sconfitta
    
    def get_assalto(self) -> list[int]:
        return self.__assalto
    
    def __set_vittoria(self, vittoria: str) -> None:
        if isinstance(vittoria, str) and vittoria.strip():    # Rimuove spazi all'inizio e alla fine
            self.__urlo_vittoria = vittoria
        else:
            self.__urlo_vittoria = "GRAAAHHH"

    def __set_sconfitta(self, sconfitta: str) -> None:
        if isinstance(sconfitta, str) and sconfitta.strip():    # Rimuove spazi all'inizio e alla fine
            self.__gemito_sconfitta = sconfitta
        else:
            self.__gemito_sconfitta = "Uuurghhh"

    def __set_assalto(self) -> None:
        self.__assalto:list[int] = []
        while len(self.__assalto) <= 15:
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
    
#===============================================================================================
    
def pariUguali(a: list[int], b: list[int]) -> list[int]:
    c:list[int] = []

    for i in range(len(a)):
        if a[i] % 2 == 0 and b[i] % 2 == 0:
            c.append(1)
        else:
            c.append(0)

    return c

def combattimento(a: Alieno, m: Mostro) -> Mostro | Alieno | None:

    if isinstance(a, Alieno) and isinstance(m, Mostro):
        if pariUguali(a.munizioni(), m.get_assalto()).count(1) >= 4:
            print(f'{m.get_urlo_vittoria()}\n'*3)
            return(m)
        else:
            print(m.get_gemito_sconfitta())
            return(a)
    else:
        print('Oggetti non validi')
        return None

def proclamaVincitore(c: Creatura) -> None:
    larghezza_totale = len(str(c)) + 10
    bordo = '*' * larghezza_totale
    riga_vuota = '*' + ' ' * (larghezza_totale - 2) + '*'
    
    # Riga con il nome centrato
    contenuto = str(c)
    spazi = larghezza_totale - 2 - len(contenuto)
    padding_sinistra = spazi // 2
    padding_destra = spazi - padding_sinistra
    riga_nome = '*' + ' ' * padding_sinistra + contenuto + ' ' * padding_destra + '*'
    
    # Stampa il tutto
    print(f"{'Gli alieni hanno vinto!' if isinstance(c, Alieno) else 'I mostri hanno vinto!'}")
    print(bordo)
    print(riga_vuota)
    print(riga_nome)
    print(riga_vuota)
    print(bordo)

#===============================================================================================

def main():
    alieno1: Alieno = Alieno(nome='Robot')
    mostro1: Mostro = Mostro(nome='gorthor')

    # 1. Stampa informazioni iniziali
    print(alieno1)  # Usa __str__
    print(f"Munizioni: {alieno1.munizioni()}\n")
    
    print(mostro1)  # Usa __str__
    print(f"Assalto: {mostro1.get_assalto()}\n")

    # 2. Combattimento
    print("Combattimento\n")

    vincitore = combattimento(alieno1, mostro1)

    # 3. Proclama vincitore
    print()
    proclamaVincitore(vincitore)



if __name__ == "__main__":
    main()