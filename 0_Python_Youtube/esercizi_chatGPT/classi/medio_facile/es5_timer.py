'''⏰ Esercizio 5 : Timer

Crea una classe Timer con:
    attributi: ore, minuti, secondi
    metodo aggiungi_secondi(n) che aggiunge n secondi e aggiorna ore/minuti di conseguenza
    metodo stampa() che mostra il tempo nel formato hh:mm:ss (es. 01:04:09)
    assicurati che i valori rimangano sempre in un formato corretto'''

class Timer:
    def __init__(self, ore=0, minuti=0, secondi=0):
        # Controlli base (se vuoi puoi aggiungerli)
        if not (0 <= ore < 24):
            raise ValueError("Ore devono essere tra 0 e 23")
        if not (0 <= minuti < 60):
            raise ValueError("Minuti devono essere tra 0 e 59")
        if not (0 <= secondi < 60):
            raise ValueError("Secondi devono essere tra 0 e 59")

        self._ore = ore
        self._minuti = minuti
        self._secondi = secondi

    def aggiungi_secondi(self, n):
        totale_secondi = self._ore * 3600 + self._minuti * 60 + self._secondi + n
        # modulo 24 ore in secondi
        totale_secondi %= 24 * 3600

        self._ore = totale_secondi // 3600
        totale_secondi %= 3600
        self._minuti = totale_secondi // 60
        self._secondi = totale_secondi % 60

    def stampa(self):
        # Formatta sempre con due cifre
        return f"{self._ore:02d}:{self._minuti:02d}:{self._secondi:02d}"


if __name__ == "__main__":
    ora = Timer(23, 59, 30)
    ora.aggiungi_secondi(90)  # aggiungo 1 minuto e 30 secondi

    print(ora.stampa())  # dovrebbe stampare 00:01:00
