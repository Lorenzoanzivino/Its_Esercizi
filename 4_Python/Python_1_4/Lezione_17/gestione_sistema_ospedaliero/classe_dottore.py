'''### CLASSE: Dottore
Creare un file chiamato "dottore.py".
In tale file, definire una classe chiamata Dottore. Si derivi Dottore dalla classe Persona.

Un dottore ha un nome, un cognome, un età, definiti dalla classe Persona, una specializzazione descritta tramite una stringa (ad esempio, Pediatra, Ostetrico, Medico Generale), ed una parcella per le visite in studio (si usi il tipo float). Gli attributi della classe dottore devono essere anch'essi privati.

- Definire i seguenti metodi:

    costruttore della classe Dottore, il quale richiede in input la specializzazione (specialization) di un dottore e la sua parcella (parcel). Tale metodo deve controllare che specialization sia una stringa e che parcel sia un float, altrimenti assegna None all'attributo che non verifica la condizione richiesta, mostrando un messaggio di errore, ad esempio, "La parcella inserita non è un float!".

    setSpecialization(specialization): consente di impostare la specializzazione di un dottore, modificando il valore del relativo attributo. Il valore viene modificato se e solo se viene passata al metodo una stringa. In caso contrario, stamapre un messaggio di errore, ad esempio "La specializzazione inserita non è una stringa!".

    setParcel(parcel): consente di impostare la parcella di un dottore, modificando il valore del relativo attributo. Il valore viene modificato se e solo se viene passato al metodo un float. In caso contrario, stamapre un messaggio di errore, ad esempio "La parcella inserita non è un float!".

    getSpecialization(): consente di ritornare la specializzazione del dottore.
    getParcel(): consente di ritornare la parcella del dottore.

    isAValidDoctor(): stabilisce se un dottore è un dottore valido; un dottore è valido se e solo se ha più di 30 anni, in quanto ha avuto il tempo necessario di compiere i suoi studi in medicina. Stampare "Doctor nome e cognome is valid!", se il dottore risulta valido. In caso contrario, stampare "Doctor nome e cognome is not valid!".

    doctorGreet():tale metodo richiama la funzione greet() della classe Persona. Poi, stampa il seguente saluto "Sono un medico {specializzazione}"'''

from classe_persona import Persona

class Dottore(Persona):
    def __init__(self, first_name, last_name, age: int, specialization: str, parcel: float) -> None:
        super().__init__(first_name, last_name)
        self.set_age(age)

        if isinstance(specialization, str):
            self.__specialization = specialization
        else:
            print("La specializzazione inserita non è una stringa!")
            self.__specialization = None

        if isinstance(parcel, float):
            self.__parcel = parcel
        else:
            print("La parcella inserita non è un float!")
            self.__parcel = None

    # Getter / Setter
    def get_specialization(self) -> str:
        return self.__specialization
        
    def set_specialization(self, new_specialization) -> None:
        if isinstance(new_specialization, str):
            self.__specialization = new_specialization
        else:
            print("La specializzazione inserita non è una stringa!")

    def get_parcel(self) -> float:
        return self.__parcel
    
    def set_parcel(self, new_parcel) -> None:
        if isinstance(new_parcel, float):
            self.__parcel = new_parcel
        else:
            print(f"La parcella inserita non è un float! Valore: {new_parcel}")

    # Metodo richiesto dalla traccia
    def is_a_valid_doctor(self) -> None:
        if self.get_age() is not None and self.get_age() > 30:
            print(f"Doctor {self.get_first_name()} {self.get_last_name()} is valid!")
        else:
            print(f"Doctor {self.get_first_name()} {self.get_last_name()} is not valid!")

    def doctor_greet(self) -> None:
        print(self.greet())
        print(f"Sono un medico {self.get_specialization()}")