'''🧠 Esercizio 1 : Classe Persona

Crea una classe chiamata Persona che abbia:
    un costruttore con i parametri: nome e età
    un metodo saluta() che stampa: "Ciao, sono <nome> e ho <età> anni"

Esempio di utilizzo:
p1 = Persona("Luca", 25)
p1.saluta()  # Output: Ciao, sono Luca e ho 25 anni'''

class Persona:
    _nome : str
    _eta : int

    def __init__(self, nome:str, eta:int) -> None:
        self.set_nome(nome)
        self.set_eta(eta)

    def get_nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome:str) -> None:
        if not isinstance(nome, str):
            raise ValueError("Il nome deve contenere solo lettere")
        self._nome = nome

    def get_eta(self) -> int:
        return self._eta
    
    def set_eta(self, eta:int) -> None:
        if eta < 0 or eta > 100:
            raise ValueError("L'età non è reale")
        else:
            self._eta = eta

    def saluta(self) -> str:
        return f"Ciao, sono {self.get_nome()} e ho {self.get_eta()} anni"
    
    def __str__(self) -> str:
        return f"nome: {self.get_nome()}, eta: {self.get_eta()}"
    

if __name__ == "__main__":

    p1 = Persona("Lorenzo", 28)
    print(p1)
    print(p1.saluta())