'''🐱 Esercizio 3 : Animali (Ereditarietà)

Crea una classe Animale con:
    attributo nome
    metodo parla() che stampa "L'animale fa un verso"

Poi crea due sottoclassi:
    Cane, che sovrascrive parla() e stampa "Bau"
    Gatto, che stampa "Miao"

Infine, crea una funzione fai_parlare(animali) che prende una lista di oggetti Animale e chiama il loro metodo parla().'''

class Animale:
    _nome:str

    def __init__(self, nome:str) -> None:
        self._nome = nome

    def get_nome(self) -> str:
        return self._nome
    
    def parla(self) -> str:
        return f"L'animale {self.get_nome()} fa un verso..."
    
class Cane(Animale):
    def __init__(self, nome:str = "cane") -> None:
        super().__init__(nome)

    def parla(self) -> str:
        return f"L'animale {self.get_nome()} fa Bau!"    


class Gatto(Animale):
    def __init__(self, nome:str = "gatto") -> None:
        super().__init__(nome)
    
    def parla(self) -> str:
        return f"L'animale {self.get_nome()} fa Miao!"    
    
def fai_parlare(animali:list[Animale]) -> None:
    for animale in animali:
        print(animale.parla())


if __name__ == "__main__":

    lista = [Cane("Astrid"), Gatto("Dusty"), Animale("Generico")]
    fai_parlare(lista)