# programmazione che prende oggetti del mondo reali e le trasforma in entità nel programma
# creare rappresentazioni di oggetti del mondo reale

# ISTANZA = DERIVA DA: oggetto dell'istanza Persona, che deriva dallo stampino Persona 

# Metodi = Azioni che farà

# Creo la classe persona
class Persona:
    _nome:str
    _cognome:str
    _eta:int
    def __init__(self, nome:str, cognome:str, eta:int) -> None:
        self._nome = nome
        self._cognome = cognome
        self._eta = eta

    def saluta(self) -> str:
        print(f"Ciao sono: {self._nome}")




# creo oggetto
persona1 = Persona("Lorenzo", "Anzivino", 28)
persona2 = Persona("Stefano", "Reali", 35)

persona1.saluta()
persona2.saluta()

persona2._nome = "Maria"
persona2.saluta()

