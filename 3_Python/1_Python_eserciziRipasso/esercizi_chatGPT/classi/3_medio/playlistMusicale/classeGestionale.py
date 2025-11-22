from classeArtista import Artista
from classeBrano import Brano

class Gestionale:
    # classe che crea dizionari dove per ogni artista ho una lista di brani
    
    _artista:Artista
    _brano:Brano
    _rubrica:dict

    def __init__(self) -> None:
        self._rubrica: dict[Artista, list[Brano]] = {}    # dizionario chiave: Artista, valore: lista di Brani

    def aggiungi_artista(self, artista: Artista) -> None:
        for a in self._rubrica.keys():
            if a.get_nomeArte() == artista.get_nomeArte():
                print(f"Artista {artista.get_nomeArte()} già presente.")
                return
        self._rubrica[artista] = []

    def rimuovi_artista(self, artista: Artista) -> None:
        for a in list(self._rubrica.keys()):
            if a.get_nomeArte() == artista.get_nomeArte():
                self._rubrica.pop(a)
                return
        print(f"Artista {artista.get_nomeArte()} non trovato.")


    def aggiungi_brano_a_artista(self, artista: Artista, brano: Brano) -> None:
        if artista in self._rubrica:
            self._rubrica[artista].append(brano)
        else:
            self._rubrica[artista] = [brano]

    def rimuovi_brano_da_artista(self, artista: Artista, brano: Brano) -> None:
        for a in self._rubrica.keys():
            if a.get_nomeArte() == artista.get_nomeArte():
                try:
                    self._rubrica[a].remove(brano)
                except ValueError:
                    print(f"Brano {brano.get_titolo()} non trovato per {a.get_nomeArte()}.")
                return
        print(f"Artista {artista.get_nomeArte()} non trovato.")

    def lista_artisti(self) -> None:
        for artista, brani in self._rubrica.items():
            print(f"Artista: {artista.get_nomeArte()} ({artista.get_nome()} {artista.get_cognome()})")
            if brani:
                for b in brani:
                    print(f"  - {b.get_titolo()} ({b.get_durata()})")
            else:
                print("  Nessun brano presente.")


    def to_dict(self) -> list:
        """
        Restituisce la rubrica come lista di dizionari:
        ogni elemento contiene il nome d'arte e la lista dei brani.
        """
        result = []
        for artista, brani in self._rubrica.items():
            result.append({
                "Artista": artista.get_nomeArte(),
                "Brani": [{"Titolo": b.get_titolo(), "Durata": b.get_durata()} for b in brani]
            })
        return result