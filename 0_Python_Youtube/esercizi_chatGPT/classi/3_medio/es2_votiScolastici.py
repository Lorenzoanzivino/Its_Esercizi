'''2. Registro di Voti Scolastici

Crea una classe Studente con nome, cognome e una lista di voti (interi da 1 a 10).
Crea una classe Registro che tiene traccia degli studenti e permette di:

    aggiungere studenti
    inserire un voto per uno studente
    calcolare la media dei voti di uno studente
    stampare tutti gli studenti con la loro media

Difficoltà: 4-5
Focus: liste, calcoli, oggetti collegati'''

class Studente:
    _nome:str
    _cognome:str
    _listaVoti:list[int] # da 1 a 10

    def __init__(self, nome:str, cognome:str) -> None:
        self._nome = nome
        self._cognome = cognome
        self._listaVoti = []

    def get_nome(self):
        return self._nome
    
    def get_cognome(self):
        return self._cognome
    
    def get_listaVoti(self):
        return self._listaVoti

    def __str__(self) -> str:
        return f"nome: {self.get_nome()}, cognome: {self.get_cognome()}"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        if not isinstance(other, Studente):
            return False
        return self.get_nome() == other.get_nome() and self.get_cognome() == other.get_cognome()



class Registro:
    _listaStudenti:list = []

    def __init__(self):
        self._listaStudenti = []

    def aggiungiStudente(self, studente:Studente):
        if studente not in self._listaStudenti:
            self._listaStudenti.append(studente)
            print(f"Aggiunto {studente}")
        else:    
            print(f"Lo studente {studente.get_nome()} già esiste")
        
    def rimuoviStudente(self, studente:Studente):
        if studente in self._listaStudenti:
            self._listaStudenti.remove(studente)
            print(f"Eliminato {studente}")
        else:
            print(f"Lo studente {studente.get_nome()} non esiste")

    def aggiungiVoto(self, studente:Studente, voto:int):
        if studente not in self._listaStudenti:
            print(f"Studente {studente.get_nome()} non presente nel registro!")
            return
        if 1 <= voto <= 10:
            studente._listaVoti.append(voto)
            print(f"Aggiunto voto {voto} a {studente.get_nome()}")
        else:
            print(f"Voto {voto} non valido. Deve essere tra 1 e 10.")

    def media(self, studente: Studente):
        voti = studente.get_listaVoti()
        if not voti:  # lista vuota
            return 0
        somma = 0
        count = 0
        for voto in voti:
            somma += voto
            count += 1
        return somma / count

    def info(self):
        print("\nLista degli studenti:")
        for studente in self._listaStudenti:
            print(f"{studente} - Media: {self.media(studente):.2f}")


registro = Registro()
s1 = Studente("Lorenzo", "Anzivino")
s2 = Studente("Stefano", "Reali")

registro.aggiungiStudente(s1)
registro.rimuoviStudente(s1)
registro.rimuoviStudente(s2)
registro.aggiungiStudente(s1)
registro.aggiungiStudente(s1)
registro.aggiungiStudente(s2)

registro.aggiungiVoto(s1, 5)
registro.aggiungiVoto(s1, 5)
registro.aggiungiVoto(s2, 8)

registro.info()

