
from classeGestionale import Artista, Brano, Gestionale

class Playlist:
    # classe per raccolta di brani
    _nome:str
    _la_mia_playlist:list

    def __init__(self, nome:str) -> None:
        self._nome = nome
        self._la_mia_playlist:list[Brano]= []

    def get_nome(self) -> str:
        return self._nome

    def get_la_mia_Playlist(self) -> list[Brano]:
        return self._la_mia_playlist

    def aggiungiBrano(self, brano: Brano, gestionale: Gestionale) -> None:
        # Lista vuota per contenere tutti i brani presenti nella rubrica
        brani_esistenti = []

        # Iteriamo su tutti i valori del dizionario della rubrica
        # Ogni valore è una lista di brani di un artista
        for lista_brani in gestionale._rubrica.values():
            for b in lista_brani:  # uso 'b' invece di 'brano' per non sovrascrivere il parametro
                brani_esistenti.append(b)

        # Ora 'brani_esistenti' contiene tutti i brani presenti nella rubrica

        if brano not in brani_esistenti:
            print(f"[AVVISO] Il brano '{brano.get_titolo()}' non esiste nella rubrica. Impossibile aggiungere.")
            return
        if brano in self._la_mia_playlist:
            print(f"[AVVISO] Il brano '{brano.get_titolo()}' è già in playlist.")
            return
        self._la_mia_playlist.append(brano)
        print(f"[INFO] Brano '{brano.get_titolo()}' aggiunto alla playlist.")


    def rimuoviBrano(self, brano:Brano) -> None:
        if brano in self._la_mia_playlist:
            self._la_mia_playlist.remove(brano)

    def __str__(self) -> str:
        # 1. Se la playlist è vuota, restituisco subito un messaggio dedicato
        if not self._la_mia_playlist:
            return f"{self.get_nome()} [Playlist vuota]"

        return f"{self.get_nome()}\n{self.get_la_mia_Playlist()}"
