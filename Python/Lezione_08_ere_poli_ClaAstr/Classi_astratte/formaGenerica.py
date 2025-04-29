from abc import ABC, abstractmethod

class FormaGenerica(ABC):

    '''
    Creare una classe formaGenerica che mi consente di:
    - Disegnare delle forme 
    - Creo il nome del metodo posticipando la sua implementazione a dopo
    '''
    
    @abstractmethod  #DECORATOR
    def draw(self) -> None:
        pass


    def setShape(self, shape:str) -> None:
        if shape:
            self.shape = shape
        else:
            print("Errore! la shape non può essere una stringa vuota")

    def getShape(self) -> str:
        return self.shape
