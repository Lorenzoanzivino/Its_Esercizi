class Alieno:

    '''
    di un alieno ci serve sapere la galassia di provenienza
    self.galaxy: str

    '''

    # Inizializzare un oggetto della classe Alieno7
    def __init__(self, galaxy:str):

        self.setGalaxy(galaxy)

    def setGalaxy(self, galaxy:str) -> None:
        if galaxy:
            self.galaxy = galaxy
        else:
            print("Errore! La galassia di provenienza deve essere una stringa vuota")

    def getGalaxy(self) -> str:
        return self.galaxy
    
    def __str__(self) -> str:
        return f"\nAlieno proveniente dalla galassia: {self.getGalaxy()}\n"
    
    
    def speak(self) -> None:
        print("\nLingua aliena: **************\n")
    
