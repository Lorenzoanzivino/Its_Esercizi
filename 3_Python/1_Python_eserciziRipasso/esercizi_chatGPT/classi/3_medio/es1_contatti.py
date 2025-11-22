'''Crea una classe Contatto con nome, numero di telefono e email.
Crea una classe Rubrica che permette di aggiungere, cercare e rimuovere contatti per nome.
Implementa metodi per stampare tutti i contatti e per aggiornare il numero o l’email di un contatto.

Difficoltà: 4
Focus: classi, liste, ricerca semplice'''

class Contatto:
    _nome:str
    _numeroTelefono:str
    _email:str

    def __init__(self, nome:str, numeroTelefono:str, email:str) -> None:
        self._nome = nome
        self.set_numeroTelefono(numeroTelefono)
        self.set_email(email)

    def get_nome(self) -> str:
        return self._nome
    
    def get_numeroTelefono(self) -> str:
        return self._numeroTelefono
    
    def get_email(self) -> str:
        return self._email
    
    def set_numeroTelefono(self, nuovo_numero: str) -> None:
        self._numeroTelefono = nuovo_numero

    def set_email(self, nuova_email: str) -> None:
        self._email = nuova_email
    
    def __str__(self) -> str:
        return f"Nome: {self.get_nome()}, Telefono: {self.get_numeroTelefono()}, Email: {self.get_email()}"
    
    def __eq__(self, other):
        if not isinstance(other, Contatto):
            return False
        if self.get_nome() == other.get_nome() and self.get_numeroTelefono() == other.get_numeroTelefono() and self.get_email() == other.get_email():
            return True
        return False

class Rubrica:
    def __init__(self) -> None:
        self.listaContatti = []
    
    def get_lista(self) -> list:
        return self.listaContatti

    def aggiungi(self, contatto: Contatto):
        if contatto in self.listaContatti:
            return f"Contatto {contatto}: già presente"
        else:
            self.listaContatti.append(contatto)
            return f"Contatto {contatto}: aggiunto"
            
    def rimuovi(self, contatto:Contatto):
        if contatto in self.listaContatti:
            self.listaContatti.remove(contatto)
            return f"Contatto {contatto}: eliminato"
        else:
            return f"Contatto {contatto}: non trovato"
        
    def aggiorna_numero_email(self, nome:str, nuovo_numero:str, nuova_email:str):
        for contatto in self.listaContatti:
            if contatto.get_nome() == nome:
                if contatto.get_numeroTelefono() != nuovo_numero:
                    contatto.set_numeroTelefono(nuovo_numero)
                if contatto.get_email() != nuova_email:
                    contatto.set_email(nuova_email)


def main():
    rubrica = Rubrica()

    # Creo alcuni contatti
    p1 = Contatto("lorenzo", "3774738083", "lorenzoanzivino@gmail.com")
    p2 = Contatto("Stefano", "3455557689", "stefano@stefano.com")
    p3 = Contatto("lorenzo", "3475622315", "lorenzorossi@gmail.com")

    # Aggiungo e rimuovo contatti alla rubrica
    print(rubrica.aggiungi(p1))  
    print(rubrica.aggiungi(p2))
    print(rubrica.aggiungi(p3))
    print(rubrica.aggiungi(p1))  # Provo a riaggiungere p1, dovrebbe avvisare
    print(rubrica.rimuovi(p2))
    print(rubrica.aggiungi(p2))

    # Stampo tutti i contatti
    print("\nContatti in rubrica:")
    for c in rubrica.get_lista():
        print(c)

    # Aggiorno numero e email di 'lorenzo'
    rubrica.aggiorna_numero_email("lorenzo", "1234567890", "nuovaemail@example.com")

    # Stampo di nuovo per vedere i cambiamenti
    print("\nContatti dopo aggiornamento:")
    for c in rubrica.get_lista():
        print(c)

if __name__ == "__main__":
    main()