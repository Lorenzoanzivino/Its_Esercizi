# Definire il dato PERSONA usando le classi.

class Persona:
    '''
    Di una persona dobbiamo sapere delle informazioni.
    Queste informazioni, vengono chiamati attributi della classe Persona
    Le informazioni sono:
    - nome
    - cognome
    - età
    
    Come si rappresentano?
    
    self.name:str (attributo di tipo stringa)
    self.lastname:str (attributo di tipo stringa)
    self.age:int (attributo di tipo int)

    self è una funzione apposita per la classe persona (in questo caso)
    '''

    # Costruttore
    # definisco il costruttore usando __init__ che ci permette di inizializzare una variabile di tipo persona
    # Senza il costruttore def __init__ la funzione displayData non funzionerebbe

    def __init__(self, name:str, lastname:str, age:int):
        # passo il valore in input al costruttore
        # self. qualcosa rappresenta l'attributo
        self.name = name 
        self.lastname = lastname
        self.age = age

    # funzione che mostri in output i dati relativi ad una persona
    def displayData(self) -> None:
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nAnni: {self.age}")