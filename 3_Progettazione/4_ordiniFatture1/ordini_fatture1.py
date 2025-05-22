
# ============================================================================================================================
# IMPORT E MODULI DI BASE
'''Importazione di moduli standard per gestione date, enumerazioni e validazione tramite espressioni regolari'''

from datetime import date
from enum import StrEnum
import re

# ============================================================================================================================

# CLASSE STRINGA
'''Classe di utilità per validare che un valore sia una stringa non vuota'''

class Stringa:
    @staticmethod
    def valida(valore):
        if not isinstance(valore, str):
            raise ValueError("Il valore deve essere una stringa")
        if not valore.strip():
            raise ValueError("La stringa non può essere vuota o solo spazi")
        return valore

# ============================================================================================================================

# CLASSE INDIRIZZO
'''Rappresenta un indirizzo con via, civico e CAP validato'''

class Indirizzo:
    _via: str
    _civico: int

    def __init__(self, via:str, civico:int, cap: str) -> None:
        self._via: str = Stringa.valida(via)
        self._civico: int = civico

        # Converti prima in stringa, poi fai i controlli:
        cap_str = str(cap)

        if len(cap_str) != 5 or not cap_str.isdigit():
            raise ValueError("Il CAP deve essere una stringa di 5 cifre numeriche")

        self._cap = cap_str

    def via(self) -> str:
        return self._via
    def civico(self) -> int:
        return self._civico
    def cap(self) -> str:
        return self._cap
    def __str__(self) -> str:
        return f"{self.via()}, {self.civico()}, CAP: {self.cap()}"
    def __eq__(self, other) -> bool:
        if not isinstance(other, Indirizzo):
            return False
        return (self.via(), self.civico(), self.cap()) == (other.via(), other.civico(), other.cap())
    def __hash__(self)->int: 
        return hash((self.via(), self.civico(), self.cap()))

# ============================================================================================================================

# CLASSE PARTITA IVA - TELEFONO - EMAIL - CF - RegEx
'''Valida e rappresenta una partita IVA (11 cifre numeriche)'''

class PartitaIVA:
    pattern = re.compile(r'^\d{11}$')
    
    def __init__(self, partitaiva: str):
        if not self.is_valid(partitaiva):
            raise ValueError(f"Partitaiva non valida: {partitaiva}")
        self.partitaiva = partitaiva

    @classmethod
    def is_valid(cls, partitaiva: str) -> bool:
        return bool(cls.pattern.fullmatch(partitaiva))

class Telefono:
    pattern = re.compile(r'^\+?\d{6,15}$')

    def __init__(self, telefono: str):
        if not self.is_valid(telefono):
            raise ValueError(f"telefono non valido: {telefono}")
        self.telefono = telefono

    @classmethod
    def is_valid(cls, telefono: str) -> bool:
        return bool(cls.pattern.fullmatch(telefono))

class Email:
    pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$')

    def __init__(self, email: str):
        if not self.is_valid(email):
            raise ValueError(f"Email non valida: {email}")
        self.value = email

    @classmethod
    def is_valid(cls, email: str) -> bool:
        return bool(cls.pattern.match(email))

class CodiceFiscale:
    pattern = re.compile(r'^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$')

    def __init__(self, cf: str):
        if not self.is_valid(cf):
            raise ValueError(f"Codice fiscale non valido: {cf}")
        self.cf = cf

    @classmethod
    def is_valid(cls, cf: str) -> bool:
        return bool(cls.pattern.fullmatch(cf))
    
    def __str__(self):
        return self.cf

# ============================================================================================================================

# CLASSE STATO ORDINE - StrEnum
'''Stato dell’ordine: in preparazione, inviato, da saldare, saldato'''

class StatoOrdine(StrEnum):
    IN_PREPARAZIONE = "inPreparazione"
    INVIATO = "inviato"
    DA_SALDARE = "daSaldare"
    SALDATO = "saldato"

# ============================================================================================================================

# CLASSE NAZIONE - REGIONE - CITTA 
'''Rappresenta il nome della Nazione, Regione e città'''

class Nazione:
    def __init__(self, nome: str):
        self.nome = Stringa.valida(nome)

class Regione:
    def __init__(self, nome: str):
        self.nome = Stringa.valida(nome)

class Citta:
    def __init__(self, nome: str):
        self.nome = Stringa.valida(nome)

# ============================================================================================================================

# CLASSE DIRETTORE
'''Rappresenta un direttore con dati personali, codice fiscale e anni di servizio'''

class Direttore:
    def __init__(self, nome: str, cognome: str, cf: CodiceFiscale, dataNascita: date, anniServizio: int):
        self.nome: str = Stringa.valida(nome)
        self.cognome: str = Stringa.valida(cognome)
        self.cf: CodiceFiscale = cf
        self.valida_data_nascita(dataNascita)
        self.dataNascita: date = dataNascita
        self.valida_anni_servizio(anniServizio)
        self.anniServizio: int = anniServizio

    def __str__(self):
        return (f"Direttore: {self.nome} {self.cognome}, CF: {self.cf}, Nato il {self.dataNascita}, Anni di servizio: {self.anniServizio}")

    @staticmethod
    def valida_data_nascita(dataNascita: date):
        if dataNascita > date.today():
            raise ValueError("La data di nascita non può essere futura.")
        
    @staticmethod
    def valida_anni_servizio(anni: int):
        if not isinstance(anni, int):
            raise ValueError("Gli anni di servizio devono essere un numero intero")
        
        if anni < 0:
            raise ValueError("Gli anni di servizio non possono essere negativi")
        
        if anni > 70:  # ad esempio un limite massimo plausibile
            raise ValueError("Gli anni di servizio non possono essere così elevati")

# ============================================================================================================================

# CLASSE DIPARTIMENTO
'''Rappresenta un dipartimento con nome e indirizzo'''

class Dipartimento:
    def __init__(self, nome: str, indirizzo: Indirizzo):
        self.nome: str = Stringa.valida(nome)
        self.indirizzo: Indirizzo = indirizzo

    def __str__(self):
        return f"Dipartimento: {self.nome}, Indirizzo: {self.indirizzo}"

# ============================================================================================================================

# CLASSE ORDINE
'''Rappresenta un ordine con data, importo imponibile, IVA, descrizione e stato'''

class Ordine:
    def __init__(self, dataStipula: date, imponibile: float, aliquotaIVA: float, descrizione: str, stato: StatoOrdine):
        self.dataStipula: date = dataStipula
        self.imponibile: float = imponibile
        self.aliquotaIVA: float = aliquotaIVA
        self.descrizione: str = Stringa.valida(descrizione)
        self.stato : StatoOrdine = stato

    def __str__(self):
        return (f"Ordine stipulato il {self.dataStipula}, Imponibile: €{self.imponibile:.2f}, Aliquota IVA: {self.aliquotaIVA}%, Descrizione: {self.descrizione}, Stato: {self.stato.value}")

# ============================================================================================================================

# CLASSE FORNITORE
'''Rappresenta un fornitore con ragione sociale, partita IVA, contatti e indirizzo'''

class Fornitore:
    def __init__(self, ragioneSociale: str, partitaIVA: PartitaIVA, indirizzo: Indirizzo, telefono: Telefono, email: Email):
        self.ragioneSociale: str = Stringa.valida(ragioneSociale)
        self.partitaIVA: PartitaIVA = partitaIVA
        self.indirizzo: Indirizzo = indirizzo
        self.telefono: Telefono = telefono
        self.email: Email = email

    def __str__(self):
        return (f"Fornitore: {self.ragioneSociale}, P.IVA: {self.partitaIVA.partitaiva}, Indirizzo: {self.indirizzo}, Telefono: {self.telefono.telefono}, Email: {self.email.value}")
    
# ============================================================================================================================

# SLOT DI TEST
'''
Istruzioni per avviare il test

1) Aprire il terminale.

2) Clonare la repository (se necessario):
    - git clone https://github.com/tuo_utente/tuo_repo.git

3) Accedere alla cartella del progetto:
    - cd percorso/del/progetto

4) Eseguire lo script Python:
    - python3.11 ordini_fatture1.py
'''

def test_tutte_le_classi_con_print():
    print("Test Stringa:")
    try:
        print(Stringa.valida("ciao"))              # dovrebbe stampare "ciao"
        print(Stringa.valida("   spazio   "))      # dovrebbe stampare "   spazio   "
        try:
            Stringa.valida("")                      # dovrebbe sollevare errore
        except ValueError as e:
            print(f"Errore atteso: {e}")
    except Exception as e:
        print(f"Errore inatteso: {e}")

    print("\nTest Indirizzo:")
    indirizzo = Indirizzo("Via Garibaldi", 25, "50100")
    print(indirizzo)  # stampa "Via Garibaldi, 25, CAP: 50100"

    print("\nTest PartitaIVA:")
    try:
        partita_iva = PartitaIVA("12345678901")
        print(partita_iva.partitaiva)  # stampa "12345678901"
        PartitaIVA("abc")               # dovrebbe sollevare errore
    except ValueError as e:
        print(f"Errore atteso: {e}")

    print("\nTest Telefono:")
    try:
        telefono = Telefono("+391234567890")
        print(telefono.telefono)       # stampa "+391234567890"
        Telefono("123")                # dovrebbe sollevare errore
    except ValueError as e:
        print(f"Errore atteso: {e}")

    print("\nTest Email:")
    try:
        email = Email("prova@mail.com")
        print(email.value)             # stampa "prova@mail.com"
        Email("invalid-email")         # dovrebbe sollevare errore
    except ValueError as e:
        print(f"Errore atteso: {e}")

    print("\nTest CodiceFiscale:")
    try:
        cf = CodiceFiscale("RSSMRA85M01H501U")
        print(cf)                     # stampa "RSSMRA85M01H501U"
        CodiceFiscale("123")          # dovrebbe sollevare errore
    except ValueError as e:
        print(f"Errore atteso: {e}")

    print("\nTest StatoOrdine:")
    stato = StatoOrdine.INVIATO
    print(stato)                      # stampa "inviato"

    print("\nTest Nazione, Regione, Citta:")
    nazione = Nazione("Italia")
    regione = Regione("Lombardia")
    citta = Citta("Milano")
    print(nazione.nome)               # stampa "Italia"
    print(regione.nome)               # stampa "Lombardia"
    print(citta.nome)                 # stampa "Milano"

    print("\nTest Direttore:")
    direttore = Direttore("Luca", "Bianchi", cf, date(1980, 5, 20), 15)
    print(direttore)                  # stampa descrizione direttore

    print("\nTest Dipartimento:")
    dip = Dipartimento("HR", indirizzo)
    print(dip)                       # stampa "Dipartimento: HR, Indirizzo: Via Garibaldi, 25, CAP: 50100"

    print("\nTest Ordine:")
    ordine = Ordine(date.today(), 1000.0, 22.0, "Acquisto materiali", StatoOrdine.SALDATO)
    print(ordine)                    # stampa descrizione ordine

    print("\nTest Fornitore:")
    fornitore = Fornitore("XYZ Spa", partita_iva, indirizzo, telefono, email)
    print(fornitore)                 # stampa descrizione fornitore

if __name__ == "__main__":
    test_tutte_le_classi_con_print()