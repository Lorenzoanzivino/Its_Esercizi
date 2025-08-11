# Ereditarietà

# Creo la classe principale Persona
class Persona:
    _nome:str
    _cognome:str
    _eta:int
    def __init__(self, nome:str, cognome:str, eta:int) -> None:
        self._nome = nome
        self._cognome = cognome
        self._eta = eta

    def saluta(self) -> str:
        print(f"Ciao sono: {self._nome} {self._cognome}, ho {self._eta} anni")

# Classe che eredità da Persona
class Insegnante(Persona):
    def __init__(self, nome, cognome, eta, materia) -> None:
        super().__init__(nome, cognome, eta)
        self.materia = materia

    def saluta(self):
        print(f"Ciao sono: {self._nome} {self._cognome}, ho {self._eta} anni e insegno {self.materia}")

    def dai_voto(self, n:int):
        self.n = n
        print(f"Bravo, un bel {self.n}")


# Creo oggetti

persona1 = Persona("Luca", "Rossi", 26)
insegnante1 = Insegnante("Stefano", "Reali", 35, "Matematica")

persona1.saluta()
insegnante1.saluta()
insegnante1.dai_voto(8)