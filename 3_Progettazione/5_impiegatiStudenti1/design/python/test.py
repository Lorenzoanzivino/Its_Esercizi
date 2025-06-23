from datetime import date
from Impiegati_studenti import *
from custom_types import IntGEZ, RealGEZ, CodiceFiscale

def main():
    # Creo un codice fiscale fittizio (supponendo che CodiceFiscale accetti stringhe)
    cf1 = CodiceFiscale("RSSMRA80A01H501U")
    cf2 = CodiceFiscale("VRNGTN75B12L219Z")

    # Creo una persona
    p = Persona(nome="Mario", cognome="Rossi", cf=cf1, dataNascita=date(1980, 1, 1), is_uomo=True, is_donna=False)
    print(p)
    print("---")

    # Creo uno studente
    matricola = IntGEZ(123456)
    s = Studente(nome="Luca", cognome="Verdi", cf=cf2, dataNascita=date(1995, 5, 20), is_uomo=True, is_donna=False, maternita=IntGEZ(0), matricola=matricola)
    print(s)
    print("---")

    # Creo un progetto
    progetto1 = Progetto("Sistema Gestionale")

    # Creo un progettista
    stipendio_progettista = RealGEZ(3000.50)
    progettista = Progettista(nome="Anna", cognome="Bianchi", cf=cf1, dataNascita=date(1985, 8, 15), is_uomo=False, is_donna=True, maternita=IntGEZ(1), stipendio=stipendio_progettista, progetto=progetto1)
    print(progettista)
    print("---")

    # Creo un direttore
    stipendio_direttore = RealGEZ(5000)
    direttore = Direttore(nome="Giovanni", cognome="Neri", cf=cf2, dataNascita=date(1975, 12, 10), is_uomo=True, is_donna=False, maternita=IntGEZ(0), stipendio=stipendio_direttore)
    print(direttore)
    print("---")

    # Controllo lista progettisti del progetto
    print(progetto1)

if __name__ == "__main__":
    main()
