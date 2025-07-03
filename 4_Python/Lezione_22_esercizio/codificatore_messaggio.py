from abc import ABC, abstractmethod

class CodificatoreMessaggio(ABC):

    @abstractmethod
    def codifica(self, testoInChiaro:str) -> str:
        pass

class DecodificatoreMessaggio(ABC):

    @abstractmethod
    def decodifica(self, testoCodificato:str) -> str:
        pass

class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, chiave:int) -> None:
        self.chiave = chiave
        self.alfabeto: str = "abcdefghijklmnopqrstuvwxyz"


    def codifica(self, testoInChiaro):
        codice_criptato = []
        for char in testoInChiaro:
            is_upper = char.isupper()
            char_lower = char.lower()
            if char_lower in self.alfabeto:
                nuovo_indice = (self.alfabeto.index(char_lower) + self.chiave) % 26
                carattere_codificato = self.alfabeto[nuovo_indice]
                if is_upper:
                    carattere_codificato = carattere_codificato.upper()
                codice_criptato.append(carattere_codificato)
            else:
                codice_criptato.append(char)
        return "".join(codice_criptato)

    def decodifica(self, testoCodificato: str) -> str:
        codice_decriptato = []
        for char in testoCodificato:
            is_upper = char.isupper()
            char_lower = char.lower()
            if char_lower in self.alfabeto:
                nuovo_indice = (self.alfabeto.index(char_lower) - self.chiave) % 26
                carattere_decriptato = self.alfabeto[nuovo_indice]
                if is_upper:
                    carattere_decriptato = carattere_decriptato.upper()
                codice_decriptato.append(carattere_decriptato)
            else:
                codice_decriptato.append(char)
        return "".join(codice_decriptato)
    
    def scrivi_su_file(self, nome_file: str, testo: str) -> None:
        with open(nome_file, "w", encoding="utf-8") as file:
            file.write(testo)
    
    def leggi_da_file(self, nome_file: str) -> str:
        with open(nome_file, "r", encoding="utf-8") as file:
            return file.read()

class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, n:int)-> None:
        self.n = n

    def _combinazione(self, testo: str) -> str:
        meta = (len(testo) + 1) // 2 
        if len(testo) % 2 == 0:
            prima_meta = testo[:meta]
            seconda_meta = testo[meta:]
        else:
            prima_meta = testo[:meta + 1] 
            seconda_meta = testo[meta + 1:]

        
        risultato = []
        for i in range(len(testo)):
            if i % 2 == 0:
                risultato.append(prima_meta[i // 2])
            else:
                risultato.append(seconda_meta[i // 2])
        return "".join(risultato)
    
    def _decodifica_combinazione(self, testo: str) -> str:
        prima_meta = []
        seconda_meta = []
        
        for i in range(len(testo)):
            char = testo[i]
            if i % 2 == 0:
                prima_meta.append(char)
            else:
                seconda_meta.append(char)
        
        return "".join(prima_meta) + "".join(seconda_meta)

    def codifica(self, testoInChiaro: str) -> str:
        testo = testoInChiaro
        for char in range(self.n):
            testo = self._combinazione(testo)
        return testo
    
    def decodifica(self, testoCodificato: str) -> str:
        testo = testoCodificato
        for char in range(self.n):
            testo = self._decodifica_combinazione(testo)
        return testo
    
    def scrivi_su_file(self, nome_file: str, testo: str) -> None:
        with open(nome_file, "w", encoding="utf-8") as f:
            f.write(testo)

    def leggi_da_file(self, nome_file: str) -> str:
        with open(nome_file, "r", encoding="utf-8") as f:
            return f.read()



def test_cifratore_a_scorrimento():
    print("Test del Cifratore a Scorrimento:")

    cifratore = CifratoreAScorrimento(chiave=3)

    # 1) Creiamo un file di input con testo in chiaro (solo la prima volta)
    testo_iniziale = "Questo è un testo di prova per il test."
    cifratore.scrivi_su_file("input.txt", testo_iniziale)

    # 2) Lettura del testo da file
    testo_in_chiaro = cifratore.leggi_da_file("input.txt")

    # 3) Codifica
    testo_codificato = cifratore.codifica(testo_in_chiaro)

    # 4) Scrittura testo codificato su file
    cifratore.scrivi_su_file("./4_Python/Lezione_22_esercizio/scorrimento.txt", testo_codificato)

    # 5) Stampa testo codificato
    print("Testo codificato:")
    print(testo_codificato)

    # 6) Decodifica
    testo_decodificato = cifratore.decodifica(testo_codificato)

    # 7) Stampa testo decodificato
    print("Testo decodificato:")
    print(testo_decodificato)


def test_cifratore_a_combinazione():
    print("\nTest del Cifratore a Combinazione:")

    cifratore = CifratoreACombinazione(n=3)

    # 1) Creiamo un file di input con testo in chiaro (solo la prima volta)
    testo_iniziale = "Questo è un testo di prova per il test."
    cifratore.scrivi_su_file("input.txt", testo_iniziale)

    # 2) Lettura del testo da file
    testo_in_chiaro = cifratore.leggi_da_file("input.txt")

    # 3) Codifica
    testo_codificato = cifratore.codifica(testo_in_chiaro)

    # 4) Scrittura testo codificato su file
    cifratore.scrivi_su_file("./4_Python/Lezione_22_esercizio/combinazione.txt", testo_codificato)

    # 5) Stampa testo codificato
    print("Testo codificato:")
    print(testo_codificato)

    # 6) Decodifica
    testo_decodificato = cifratore.decodifica(testo_codificato)

    # 7) Stampa testo decodificato
    print("Testo decodificato:")
    print(testo_decodificato)


if __name__ == "__main__":
    test_cifratore_a_scorrimento()
    test_cifratore_a_combinazione()