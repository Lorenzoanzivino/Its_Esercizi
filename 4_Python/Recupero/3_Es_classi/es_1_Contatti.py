'''Sviluppa un sistema per la gestione dei contatti in Python che permetta agli utenti di creare, modificare, e cercare contatti basati sui numeri di telefono. Il sistema dovrà essere capace di gestire una collezione (dizionario) di contatti e i loro numeri di telefono.
    1. Classe ContactManager:
    Gestisce tutte le operazioni legate ai contatti.
    Attributi:
        ● contacts: dict[str, list[str]] - Dizionario che ha per chiave il nome del contatto e per valore una lista di numeri di telefono. I numeri di telefono sono espressi sottoforma di stringa.
    Metodi:
        ● create_contact(name: str, phone_numbers: list[str]): Crea un nuovo contatto, aggiungendolo al dizionario contacts con il nome specificato e una lista di numeri di telefono. Restituisce un nuovo dizionario con il solo contatto appena creato o il messaggio di errore "Errore: il contatto esiste già." se il contatto esiste già.
        ● add_phone_number(contact_name: str, phone_number: str): Aggiunge un numero di telefono al contatto specificato. Restituisce un nuovo dizionario con il solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il contatto non esiste oppure "Errore: il numero di telefono esiste già." se il numero di telefono è già presente per il contatto specificato.
        ● remove_phone_number(contact_name: str, phone_number: str): Rimuove un numero di telefono dal contatto specificato. Restituisce un nuovo dizionario con il solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il contatto non esiste oppure "Errore: il numero di telefono non è presente." se il numero di telefono non esiste per il contatto specificato.
        ● update_phone_number(contact_name: str, old_phone_number: str, new_phone_number: str): Sostituisce un numero di telefono con un altro nel contatto specificato. Restituisce un nuovo dizionario con il solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il contatto non esiste oppure "Errore: il numero di telefono non è presente." se il numero di telefono non esiste per il contatto specificato.
        ● list_contacts(): Ritorna una lista di tutte le chiavi all'interno del dizionario contacts.
        ● list_phone_numbers(contact_name: str): Mostra i numeri di telefono di un contatto specifico. Restituisce la lista dei numeri di telefono o il messaggio dierrore "Errore: il contatto non esiste." se il contatto non esiste.
        ● search_contact_by_phone_number(phone_number: str): Trova e restituisce tutti i contatti che contengono un determinato numero di telefono. Restituisce una lista di tutte le chiavi all'interno del dizionario contacts che hanno il numero specificato tra i valori oppure il messaggio di errore "Nessun contatto trovato con questo numero di telefono." se nessun contatto contiene il numero di telefono.'''

class ContactManager:
    def __init__(self) -> None:
        self.contacts: dict[str, list[str]] = {}

    def create_contact(self, name: str, phone_numbers: list[str]) -> dict[str, list[str]] | str:
        if name not in self.contacts:
            self.contacts[name] = phone_numbers
            return {name: phone_numbers}
        return "Errore: il contatto esiste già."

    def add_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]] | str:
        if contact_name not in self.contacts:
            return "Errore: il contatto non esiste."
        if phone_number in self.contacts[contact_name]:
            return "Errore: il numero di telefono esiste già."
        self.contacts[contact_name].append(phone_number)
        return {contact_name: self.contacts[contact_name]}

    def remove_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]] | str:
        if contact_name not in self.contacts:
            return "Errore: il contatto non esiste."
        if phone_number not in self.contacts[contact_name]:
            return "Errore: il numero di telefono non è presente."
        self.contacts[contact_name].remove(phone_number)
        return {contact_name: self.contacts[contact_name]}

    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str) -> dict[str, list[str]] | str:
        if contact_name not in self.contacts:
            return "Errore: il contatto non esiste."
        if old_phone_number not in self.contacts[contact_name]:
            return "Errore: il numero di telefono non è presente."
        self.contacts[contact_name].remove(old_phone_number)
        if new_phone_number not in self.contacts[contact_name]:
            self.contacts[contact_name].append(new_phone_number)
        return {contact_name: self.contacts[contact_name]}

    def list_contacts(self) -> list[str]:
        return list(self.contacts.keys())

    def list_phone_numbers(self, contact_name: str) -> list[str] | str:
        if contact_name not in self.contacts:
            return "Errore: il contatto non esiste."
        return self.contacts[contact_name]

    def search_contact_by_phone_number(self, phone_number: str) -> list[str] | str:
        result = []
        for name, numbers in self.contacts.items():
            if phone_number in numbers:
                result.append(name)
        if result:
            return result
        else:
            return "Nessun contatto trovato con questo numero di telefono."

def run_tests():
    cm = ContactManager()

    # Test 1: Creazione contatto
    print("Test 1:", cm.create_contact("Mario Rossi", ["123456789"]))  
    # Atteso: {'Mario Rossi': ['123456789']}

    # Test 2: Creazione contatto esistente
    print("Test 2:", cm.create_contact("Mario Rossi", ["987654321"]))  
    # Atteso: "Errore: il contatto esiste già."

    # Test 3: Aggiunta numero telefono a contatto esistente
    print("Test 3:", cm.add_phone_number("Mario Rossi", "987654321"))  
    # Atteso: {'Mario Rossi': ['123456789', '987654321']}

    # Test 4: Aggiunta numero duplicato
    print("Test 4:", cm.add_phone_number("Mario Rossi", "123456789"))  
    # Atteso: "Errore: il numero di telefono esiste già."

    # Test 5: Rimozione numero telefono
    print("Test 5:", cm.remove_phone_number("Mario Rossi", "123456789"))  
    # Atteso: {'Mario Rossi': ['987654321']}

    # Test 6: Rimozione numero non presente
    print("Test 6:", cm.remove_phone_number("Mario Rossi", "000000000"))  
    # Atteso: "Errore: il numero di telefono non è presente."

    # Test 7: Aggiornamento numero telefono
    print("Test 7:", cm.update_phone_number("Mario Rossi", "987654321", "111222333"))  
    # Atteso: {'Mario Rossi': ['111222333']}

    # Test 8: Aggiornamento numero non presente
    print("Test 8:", cm.update_phone_number("Mario Rossi", "987654321", "444555666"))  
    # Atteso: "Errore: il numero di telefono non è presente."

    # Test 9: Lista contatti
    print("Test 9:", cm.list_contacts())  
    # Atteso: ['Mario Rossi']

    # Test 10: Lista numeri telefono
    print("Test 10:", cm.list_phone_numbers("Mario Rossi"))  
    # Atteso: ['111222333']

    # Test 11: Lista numeri telefono contatto non esistente
    print("Test 11:", cm.list_phone_numbers("Luigi Bianchi"))  
    # Atteso: "Errore: il contatto non esiste."

    # Test 12: Ricerca contatti per numero
    print("Test 12:", cm.search_contact_by_phone_number("111222333"))  
    # Atteso: ['Mario Rossi']

    # Test 13: Ricerca contatti per numero non esistente
    print("Test 13:", cm.search_contact_by_phone_number("000000000"))  
    # Atteso: "Nessun contatto trovato con questo numero di telefono."

run_tests()
