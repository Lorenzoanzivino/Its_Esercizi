'''Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo. Questa classe dovrebbe ridefinire il metodo dettagliPagamento() per indicare che il pagamento è in contanti. Si definisca inoltre il metodo inPezziDa() che stampa a schermo quante banconote da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro, 5 euro e/o in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro sono necessarie per pagare l'importo in contanti.'''

from pagamento import Pagamento

class PagamentoContanti(Pagamento):
    def __init__(self):
        super().__init__()

    def dettagliPagamento(self) -> None:
        print(f"L'importo del pagamento: €{round(self.getImporto(), 2)} è in contanti")

    def inPezziDa(self) -> None:
        importo = self.getImporto()
        banconote = [500, 200, 100, 50, 20, 10, 5]
        monete = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.01]

        print(f"Pagare €{importo:.2f} in contanti con:")
    
        for taglio in banconote:
            num = int(importo // taglio)
            if num > 0:
                print(f"{num} banconota/e da €{taglio}")
                importo -= num * taglio

        for taglio in monete:
            num = int(importo // taglio)
            if num > 0:
                print(f"{num} moneta/e da €{taglio}")
                importo -= num * taglio
                importo = round(importo, 2)

if __name__ == '__main__':
    pagamento1 = PagamentoContanti()
    pagamento1.setImporto(999.99)

    pagamento1.inPezziDa()