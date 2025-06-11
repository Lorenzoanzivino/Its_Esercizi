from __future__ import annotations

# SLIDE 63

class Studente:
    _nome:str
    _esami:list[Esame]

    def __init__(self, nome:str) -> None:
        self.set_nome(nome)
        self._esami = []

    def get_nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome) -> None:
        self._nome = nome

    def aggiungi_esame(self, esame: 'Esame') -> None:
        for esame_esistente in self.get_esami():
            if esame_esistente.get_modulo() == esame.get_modulo():
                raise RuntimeError(f"Errore: esame già presente per il modulo {esame_esistente.get_modulo()}")
        self._esami.append(esame)


    def get_esami(self) -> list:
        return self._esami
    
    def calcola_media(self) -> float:
        if not self._esami:
            return 0.0
        totale = sum(esame.get_voto() for esame in self._esami)
        return totale / len(self._esami)
        

class Modulo:
    _codice:str

    def __init__(self, codice:str) -> None:
        self.set_codice(codice)

    def get_codice(self) -> str:
        return self._codice
    
    def set_codice(self, codice:str) -> None:
        self._codice = codice

class Esame:
    _voto: int
    _studente: Studente
    _modulo: Modulo

    def __init__(self, voto: int, studente: Studente, modulo: Modulo) -> None:
        self.set_voto(voto)
        self.set_studente(studente)
        self.set_modulo(modulo)

    def get_voto(self) -> int:
        return self._voto
    
    def set_voto(self, voto: int) -> None:
        self._voto = voto

    def get_studente(self) -> Studente:
        return self._studente
    
    def set_studente(self, studente: Studente) -> None:
        self._studente = studente
    
    def get_modulo(self) -> Modulo:
        return self._modulo
    
    def set_modulo(self, modulo: Modulo) -> None:
        self._modulo = modulo


if __name__ == '__main__':
    studente1 = Studente("Luca Rossi")
    modulo1 = Modulo("MAT101")
    esame1 = Esame(28, studente1, modulo1)
    esame2 = Esame(21, studente1, modulo1)

    print("Proviamo ad aggiungere esame1")
    studente1.aggiungi_esame(esame1)
    print("OK\n")
    try:
        print("Proviamo ad aggiungere esame2")
        studente1.aggiungi_esame(esame2)
        print("OK")
    except RuntimeError:
        print("Ci siamo accorti dell'errore!\n")

    print(f"Studente: {esame1.get_studente().get_nome()}")
    print(f"Modulo: {esame1.get_modulo().get_codice()}")
    print(f"Voto: {esame1.get_voto()}")
    print(f"Voto: {esame2.get_voto()}")
    print(f"La media di {studente1.get_nome()} è {studente1.calcola_media()}\n")


    print("Stampiamo tutti gli esami effettivamente aggiunti a studente1:")
    for esame in studente1.get_esami():
        print(f"\tEsame in {esame.get_modulo().get_codice()} con voto {esame.get_voto()}")
