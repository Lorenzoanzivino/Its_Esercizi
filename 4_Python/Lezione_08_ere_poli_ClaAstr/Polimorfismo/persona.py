class Persona:
    def __init__(self,nome:str, cognome:str, eta:int):
        self.setName(nome)
        self.setCognome(cognome)
        self.setEta(eta)

    def __call__(self)->None:
        if self.eta < 18:
            print(f"{self.nome} {self.cognome} e' minorenne!")
        elif 18 <= self.eta < 30:
            print(f"{self.nome} {self.cognome} e' maggiorenne!")
        elif 30<= self.eta < 80:
            print(f"{self.nome} {self.cognome} e' una persona adulta!")
        else:
            print(f"{self.nome} {self.cognome} e' una persona anziana!") 
    
    def __str__(self) -> str:
        return f"Nome: {self.nome}\nCognome: {self.cognome}\nEtà: {self.eta}"  

    def setName(self,nome)->None:
        if nome:
            self.nome = nome
        else:
            print("Errore, il nome deve essere una stringa")

    def setCognome(self, cognome)->None:
        if cognome:
            self.cognome = cognome
        else:
            print("Errore, il cognome deve essere una stringa")

    def setEta(self,eta)->None:
        if  eta < 0 or eta > 130:
            self.eta = 0
        else:
            self.eta = eta  

    def getName(self)-> str:
        return self.nome
    def getCognome(self)->str:
        return self.cognome
    def getEta(self)->int:
        return self.eta

    # Metodo speak() per la classe Persona che consente di simulare un saluto
    def speak(self) -> None:
        print(f"\nHello! my name is {self.getName()}!\n")