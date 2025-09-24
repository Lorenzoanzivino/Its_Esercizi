'''Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e che definisce l'importo. Questa classe deve contenere gli attributi per il nome del titolare della carta, la data di scadenza, e il numero della carta di credito. Infine, si ridefinisca il metodo dettagliPagamento() per includere tutte le informazioni della carta di credito oltre all'importo del pagamento.'''

from pagamento import Pagamento

class PagamentoCartaDiCredito(Pagamento):
    __nomeTitolare:str
    __dataScadenza:str
    __numeroCarta:str

    def __init__(self, nomeTitolare:str, dataScadenza:str, numeroCarta:str) -> None:
        super().__init__()

        self.__nomeTitolare = nomeTitolare
        self.__dataScadenza = dataScadenza
        self.__numeroCarta = numeroCarta

    def getNomeTitolare(self) -> str:
        return self.__nomeTitolare
    
    def getDataScadenza(self) -> str:
        return self.__dataScadenza

    def getNumeroCarta(self) -> str:
        return self.__numeroCarta
    

    def dettagliPagamento(self) -> None:
        numero_mascherato = '*'*12 + self.getNumeroCarta()[-4:]    # primi 12 asterischi + ultime 4 cifre del numero della carta
        print(f"L'importo del pagamento: €{self.getImporto():.2f} con carta di credito: {self.getNomeTitolare()}, {numero_mascherato}, scadenza {self.getDataScadenza()}")

if __name__ == '__main__':
    pagamento1 : PagamentoCartaDiCredito = PagamentoCartaDiCredito("Lorenzo Anzivino", "09-09-2028", "CA0EZ")
    pagamento1.setImporto(999.99)

    pagamento1.dettagliPagamento()