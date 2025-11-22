'''🧩 Esercizio – Gestione Studenti
Descrizione:
    Realizza una classe chiamata ClasseStudenti che permetta di gestire un insieme di studenti e i loro voti.
    Ogni studente è rappresentato tramite un dizionario che contiene il nome dello studente e la lista dei suoi voti.
    La classe deve gestire una lista di dizionari come archivio interno.
Requisiti:
    La classe deve possedere un attributo interno chiamato studenti, che contiene una lista di dizionari.
    Ogni dizionario rappresenta uno studente con questa struttura:
    {"nome": str, "voti": list[int]}

Implementa almeno i seguenti metodi:
    aggiungi_studente(nome) – aggiunge un nuovo studente con lista voti vuota.
    aggiungi_voto(nome, voto) – aggiunge un voto allo studente indicato.
    media_studente(nome) – calcola e restituisce la media dei voti dello studente.
    elenco_medie() – restituisce un dizionario con le medie di tutti gli studenti nel formato {nome: media}.

Obiettivo:
    Simulare un piccolo sistema di gestione di una classe scolastica, usando:
    classi per la struttura logica,
    liste per memorizzare più studenti,
    dizionari per rappresentare i dati di ciascuno studente.'''

class ClasseStudenti:
    def __init__(self) -> None:
        self.lista_studenti:list[dict] = []
        self.studente:dict[str, list[int]] = {}
    
    def add_studenti(self, nome:str) -> None:
        if self.studente[nome] not in self.lista_studenti:
            self.lista_studenti.append(nome)
    
    def add_voto(self, nome:str, voto:int):
        if self.studente[nome] in self.lista_studenti:
            self.studente[nome] = voto

    def media_studente(self, nome):
        somma:int = 0
        media:float = 0
        if self.studente[nome] in self.lista_studenti:
            for self.studente[]