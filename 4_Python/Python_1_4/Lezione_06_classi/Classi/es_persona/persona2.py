
class Persona:
    # 1 costruttore
    def __init__(self):
        self.name:str = ""
        self.lastname:str = ""
        self.age:int = 0

    # 2 funzione che mostri in output i dati relativi ad una persona
    def displayData(self) -> None:
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nAnni: {self.age}")

    # 3 SET metodo che mi consenta di impostare/modificare i valori di self.name
    def setName(self, name:str) -> None:
        self.name = name
    
    # 3.2 Funzione che mi consenta di impostare il valore dell'attributo self.lastname
    def setLastname(self, lastname:str) -> None:
        self.lastname = lastname

    # 3.3 Funzione che mi consenta di impostare il valore dell'attributo self.age
    def setAge(self, age:int) -> None:
        # se il numero fosse minore a 0 o superiore ad una età improbabile, l'eta torna ad un valore 0
        if age < 0 or age > 130:
            self.age = 0
        else:
            self.age = age

    # 4 GET metodo che mi consente di ritornarne il valore di self.name
    def getName(self) -> str:
        return self.name
    
    # 4.2 funzione che mi consente di ritornarne il valore di self.lastname
    def getLastname(self) -> str:
        return self.lastname
    
    # 4.3 funzione che mi consente di ritornarne il valore di self.age
    def getAge(self) -> int:
        return self.age