# Esercizio: Sistema di Gestione di un Parco Divertimenti (OOP + Flask)
'''Classe Ride
La classe Ride rappresenta un’attrazione generica del parco. È una classe astratta e non può essere istanziata direttamente.'''

from abc import ABC, abstractmethod

class Ride(ABC):
    id:str
    name:str
    min_height_cm:int

    def __init__(self, id:str, name:str, min_height_cm:int) -> None:
        self.id = id
        self.name = name
        self.min_height_cm = min_height_cm
    
    @abstractmethod
    def category(self):
        pass

    @abstractmethod
    def base_wait(self) -> int:
        pass

    def info(self) -> dict:
        dict_info:dict = {
            "id": self.id,
            "name": self.name,
            "min_height_cm": self.min_height_cm,
            "category": self.category(),
            "base_wait": self.base_wait()
        }
        return dict_info
        
    def wait_time(self, crowd_factor: float = 1.0) -> int:
        return int(round(self.base_wait() * crowd_factor))

    def __repr__(self):
        return f"Ride: {self.name} (ID: {self.id})"
    

'''Classe RollerCoaster
La classe RollerCoaster rappresenta una montagna russa e eredita da Ride.'''

class RollerCoaster(Ride):
    inversions:int

    def __init__(self, id, name, min_height_cm, inversions:int) -> None:
        super().__init__(id, name, min_height_cm)
        self.inversions = inversions

    def category(self):
        return "roller_coaster"
    
    def base_wait(self):
        return 40 + (self.inversions * 3)
    
    def info(self):
        dict_info = super().info()

        dict_info['inversions'] = self.inversions

        return dict_info
    
'''Classe Carousel
La classe Carousel rappresenta una giostra con animali e eredita da Ride.'''

class Carousel(Ride):
    animals:list
    
    def __init__(self, id: str, name: str, min_height_cm: int, animals:list = None) -> None:
        super().__init__(id, name, min_height_cm)
        
        if animals is None:
            self.animals = ["horse", "swan", "tiger"]
        else:
            self.animals = animals

    def category(self):
        return "family"
    
    def base_wait(self):
        return 10
    
    def info(self):
        dict_info = super().info()

        dict_info['animals'] = self.animals

        return dict_info
    
class Park:
    rides:dict[str, Ride]

    def __init__(self) -> None:
        self.rides = {}

    def add(self, ride:Ride) -> None:
        if ride.id not in self.rides:
            self.rides[ride.id] = ride
        else:
            print(f"Attenzione: L'attrazione con ID {ride.id} è già presente.")

    def get(self, ride_id:str) -> Ride | None:
        return self.rides.get(ride_id)
    
    def list_all(self) -> list[Ride]:
        self.lista_attrazioni:list = []

        for ride in self.rides.values():
            self.lista_attrazioni.append(ride)

        return self.lista_attrazioni