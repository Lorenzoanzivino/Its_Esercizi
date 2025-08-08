'''🎓 Esercizio 4 – Studente e Media

Crea una classe Studente con:
    attributi: nome, voti (una lista di voti interi)
    metodo aggiungi_voto(voto)
    metodo media() che restituisce la media dei voti (arrotondata a 2 cifre)
    metodo info() che stampa nome, voti e media
'''

class Studente:
    _nome:str
    _voti:list[int]

    def __init__(self, nome:str) -> None:
        self._nome = nome
        self._voti = []

    def get_nome(self) -> str:
        return self._nome
    
    def get_voti(self) -> list:
        return self._voti
    
    def aggiungi_voto(self, voto:int) -> None:
        if not isinstance(voto, int):
            raise ValueError("Il voto deve essere un numero intero")
        self._voti.append(voto)

    def media(self) -> float:
        somma:int = 0
        count:int = 0
        media:float = 0
        for voto in self._voti:
            if self._voti == []:
                return 0.0
            else:
                somma += voto
                count += 1
            media = somma/count

        return media
    
    def info(self) -> str:
        return f"Lo studente: {self.get_nome()} con voti: {self.get_voti()}, ha una media di {self.media():.2f}"
    
if __name__ == "__main__":

    s1 = Studente("Lorenzo Anzivino")
    s1.aggiungi_voto(28)
    s1.aggiungi_voto(22)
    print(s1.info())

    s2 = Studente("Stefano Reali")
    s2.aggiungi_voto(30)
    s2.aggiungi_voto(18)
    print(s2.info())

    s3 = Studente("Veronica Ribichini")
    print(s3.info())



