'''es 4.Database di Date

Scrivi una classe che gestisca un database di date nel formato gg.mm.aaaa, implementando i seguenti metodi:

    Aggiungere una nuova data

    Eliminare una data specificata

    Modificare una data

    Effettuare una ricerca su una data specificata per ottenere una nuova data

Nota: una data deve essere un oggetto nel database e deve essere istanziata da una stringa.'''

class Date:
    def __init__(self, date_str):
        # date_str atteso nel formato 'gg.mm.aaaa'
        self.date_str = date_str
        self.giorno, self.mese, self.anno = map(int, date_str.split('.'))

    def __eq__(self, other):
        return (self.giorno == other.giorno and
                self.mese == other.mese and
                self.anno == other.anno)

    def __str__(self):
        return self.date_str

    def update(self, new_date_str):
        self.date_str = new_date_str
        self.giorno, self.mese, self.anno = map(int, new_date_str.split('.'))

class DateDatabase:
    def __init__(self):
        self.dates = []

    def aggiungi(self, date_str):
        nuova_data = Date(date_str)
        self.dates.append(nuova_data)
        print(f"Data {date_str} aggiunta.")

    def elimina(self, date_str):
        da_eliminare = Date(date_str)
        for data in self.dates:
            if data == da_eliminare:
                self.dates.remove(data)
                print(f"Data {date_str} eliminata.")
                return
        print(f"Data {date_str} non trovata.")

    def modifica(self, old_date_str, new_date_str):
        da_modificare = Date(old_date_str)
        for data in self.dates:
            if data == da_modificare:
                data.update(new_date_str)
                print(f"Data {old_date_str} modificata in {new_date_str}.")
                return
        print(f"Data {old_date_str} non trovata per modifica.")

    def cerca(self, date_str):
        da_cercare = Date(date_str)
        for data in self.dates:
            if data == da_cercare:
                print(f"Data {date_str} trovata: {data}")
                return data
        print(f"Data {date_str} non trovata.")
        return None

    def mostra(self):
        print("Date nel database:")
        for data in self.dates:
            print(f" - {data}")

# Esempio di utilizzo
db = DateDatabase()
db.aggiungi("12.05.2023")
db.aggiungi("01.01.2024")
db.mostra()
db.modifica("12.05.2023", "13.05.2023")
db.elimina("01.01.2024")
db.cerca("13.05.2023")
db.mostra()
