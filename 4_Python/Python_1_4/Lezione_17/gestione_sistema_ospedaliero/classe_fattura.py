'''### CLASSE: Fattura
Creare un file chiamato "fatture.py".
In tale file, creare una classe chiamata Fattura.

- Definire i seguenti metodi:

    init(patient,doctor): deve avere come input una lista di pazienti ed un dottore. Tale metodo deve verificare se il dottore può esercitare la professione, richiamando la funzione isAValidDoctor(). In caso affermativo assegnare all'attributo fatture (di tipo intero) il numero di pazienti che ha il dottore, mentre assegnare 0 all'attributo salary (di tipo int).  In caso contrario, assegnare il valore None a tutti i 4 gli attributi della classe e stampare un messaggio di errore, come, ad esempio: "Non è possibile creare la classe fattura poichè il dottore non è valido!".

    getSalary(): deve ritornare il salario guadagnato dal dottore. Il salario gudaganto viene calcolato moltiplicando la parcella del dottore per il numero di pazienti.

    getFatture(): deve assegnare all'attributo fatture il numero di pazienti (in modo che sia sempre aggiornato) che ha il dottore e ritornare il suo valore.

    addPatient(newPatient): consente di aggiungere un paziente alla lista di pazienti di un dottore, aggiornando poi il numero di fatture ed il salario, richiamando il metodo getFatture() e getSalary().  Stampare "Alla lista del Dottor cognome è stato aggiunto il paziente {codice_identificativo}"

    removePatient(idCode): consente di rimuovere un paziente alla lista di pazienti di un dottore ricevendo in input il codice identificativo del paziente da rimuovere, aggiornando poi il numero di fatture e il salario, richiamando il metodo get Fatture() e getSalary(). Stampare "Alla lista del Dottor cognome è stato rimosso il paziente {codice_identificativo}".'''

from classe_dottore import Dottore
from classe_paziente import Paziente

class Fattura:
    def __init__(self, patients: list[Paziente], doctor: Dottore) -> None:
        if doctor.isAValidDoctor():
            self.__lista_pazienti = patients
            self.__dottore = doctor
            self.__fatture = len(patients)
            self.__salary = 0
        else:
            print("Non è possibile creare la classe fattura poiché il dottore non è valido!")
            self.__lista_pazienti = None
            self.__dottore = None
            self.__fatture = None
            self.__salary = None

    def get_salary(self) -> float:
        if self.__dottore and self.__lista_pazienti:
            self.__salary = self.__dottore.get_parcel() * len(self.__lista_pazienti)
            return self.__salary
        return None

    def get_fatture(self) -> int:
        if self.__lista_pazienti:
            self.__fatture = len(self.__lista_pazienti)
            return self.__fatture
        return None

    def add_patient(self, new_patient: Paziente) -> None:
        if new_patient not in self.__lista_pazienti:
            self.__lista_pazienti.append(new_patient)
            self.get_fatture()
            self.get_salary()
            print(f"Alla lista del Dottor {self.__dottore.get_last_name()} è stato aggiunto il paziente {new_patient.get_id_code()}")

    def remove_patient(self, id_code: str) -> None:
        for patient in self.__lista_pazienti:
            if patient.get_id_code() == id_code:
                self.__lista_pazienti.remove(patient)
                self.get_fatture()
                self.get_salary()
                print(f"Alla lista del Dottor {self.__dottore.get_last_name()} è stato rimosso il paziente {patient.get_id_code()}")
                return
        print(f"Nessun paziente con ID {id_code} trovato nella lista.")
