'''### CLASSE: Paziente
Creare un file chiamato "paziente.py".
In tale file, creare una classe chiamata Paziente. Si derivi Paziente dalla classe Persona.

Un paziente ha un nome, un cognome, un età, definiti dalla classe Persona ed un codice identificativo (si usi il tipo String).
- Definire i seguenti metodi:

    costruttore della classe paziente, il quale richiede in input il codice identificativo, il quale deve essere un attributo privato.
    setIdCode(idCode): consente di impostare il codice identificativo del paziente.
    getidCode(): consente di ritornare il codice identificativo del paziente.
    patientInfo(): stampa in output le informazioni del paziente in questo modo:

        "Paziente: {nome} {cognome}
         ID: {codice identificativo}"'''

from classe_persona import Persona

class Paziente(Persona):
    def __init__(self, first_name, last_name, age: int, id_code: str) -> None:
        super().__init__(first_name, last_name)
        self.set_age(age)

        if isinstance(id_code, str):
            self.__id_code = id_code
        else:
            print("Il codice identificativo non è una stringa")
            self.__id_code = None

    def get_id_code(self) -> str:
        return self.__id_code

    def set_id_code(self, new_id_code: str) -> None:
        if isinstance(new_id_code, str):
            self.__id_code = new_id_code
        else:
            print("Il codice identificativo deve essere una stringa")

    def patient_info(self) -> None:
        print(
            f"Paziente: {self.get_first_name()} {self.get_last_name()} "
            f"(Età: {self.get_age()})\n"
            f"ID: {self.get_id_code()}"
        )