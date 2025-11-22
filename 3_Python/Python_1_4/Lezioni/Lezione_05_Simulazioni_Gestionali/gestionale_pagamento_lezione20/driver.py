'''Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo PagamentoCartaDiCredito con valori differenti e si invochi dettagliPagamento() per ognuno di essi.

Esempio di output:
Pagamento in contanti di: €150.00
150.00 euro da pagare in contanti con:
1 banconota da 100 euro
1 banconota da 50 euro

Pagamento in contanti di: €95.25
95.25 euro da pagare in contanti con:
1 banconota da 50 euro
2 banconote da 20 euro
1 banconota da 5 euro
1 moneta da 0.2 euro
1 moneta da 0.05 euro

Pagamento di: €200.00 effettuato con la carta di credito
Nome sulla carta: Mario Rossi
Data di scadenza: 12/24
Numero della carta: 1234567890123456

Pagamento di: €500.00 effettuato con la carta di credito
Nome sulla carta: Luigi Bianchi
Data di scadenza: 01/25
Numero della carta: 6543210987654321'''

from pagamentoContanti import PagamentoContanti
from pagamentoCartaDiCredito import PagamentoCartaDiCredito

pagamento1 : PagamentoContanti = PagamentoContanti()
pagamento1.setImporto(150.00)
pagamento1.inPezziDa()

pagamento2 : PagamentoContanti = PagamentoContanti()
pagamento1.setImporto(95.25)
pagamento1.inPezziDa()

pagamento3 : PagamentoCartaDiCredito = PagamentoCartaDiCredito("Mario Rossi", "12/24", "1234567890123456")
pagamento3.setImporto(200.00)
pagamento3.dettagliPagamento() 

pagamento4 : PagamentoCartaDiCredito = PagamentoCartaDiCredito("Luigi Bianchi", "01/25", "6543210987654321")
pagamento4.setImporto(500.00)
pagamento4.dettagliPagamento() 
