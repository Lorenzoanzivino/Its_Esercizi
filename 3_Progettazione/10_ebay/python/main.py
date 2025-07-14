from classi import *
from datetime import datetime, timedelta

anna = Privato("Anna23", datetime(2023, 6, 1, 9, 0, 0, 0))
bob = Privato("Bob77", datetime(2024, 12, 4, 12, 10, 0, 0))
# bob = Privato("Bob77", datetime(2024, 1, 24, 10, 34, 5, 0)) # Username già esistente: da un errore
charley = Privato("ItsCharley04", datetime(2024, 10, 3, 10, 13, 0, 0))
david = Privato("__DavidX__", datetime(2022, 1, 20, 8, 45, 0))
eve = Privato("xXEveTheGoodXx", datetime(2023, 5, 5, 14, 0, 0))

for utente in Privato.all():
    print(utente)

# Creazione aste
asta1 = Asta(
    descrizione="iPhone Bianco",
    anni_garanzia=IntGEZ(1),
    prezzo_iniziale=RealGEZ(350.00),
    prezzo_rialzi=RealGZ(10.00),
    scadenza=datetime.now() - timedelta(days=5))

asta2 = Asta(
    descrizione="Samsung Galaxy Costoso",
    anni_garanzia=IntGEZ(2),
    prezzo_iniziale=RealGEZ(1200.00),
    prezzo_rialzi=RealGZ(50.00),
    scadenza=datetime.now() + timedelta(days=7))

assert asta1.scaduto()
assert not asta2.scaduto()
# print(asta1)
# print(asta2)

# asta1.set_scadenza(datetime(2100, 10, 30, 12, 34, 10, 20)) # Can't set attribute 'scadenza' of an Asta that has already ended.
# asta1.set_prezzo(RealGEZ(100)) # AttributeError: Can't set attribute 'prezzo' of an Asta that has already ended.
# asta1.set_prezzo_bid(RealGEZ(20)) # Can't set attribute 'prezzo_bid' of an Asta that has already ended.
asta2.set_prezzo_bid(RealGZ(20))
# asta2.set_scadenza(datetime.now() - timedelta(days=9)) # Can't set attribute 'scadenza' of Asta to a date that is before today

print("\nGestione bid")
bid0: Bid = Bid(datetime(2023, 1, 10, 9, 30), anna, asta1)
bid1: Bid = Bid(datetime(2023, 2, 14, 14, 15), anna, asta2)
bid2: Bid = Bid(datetime(2023, 3, 5, 11, 0), anna, asta1)
bid3: Bid = Bid(datetime(2023, 4, 20, 17, 45), bob, asta2)
bid4: Bid = Bid(datetime(2023, 5, 25, 8, 20), bob, asta2)
bid5: Bid = Bid(datetime(2023, 6, 30, 16, 0), bob, asta1)
bid6: Bid = Bid(datetime(2023, 7, 12, 10, 10), bob, asta1)
bid7: Bid = Bid(datetime(2023, 8, 8, 13, 50), charley, asta2)
bid8: Bid = Bid(datetime(2023, 9, 19, 15, 30), david, asta2)
bid9: Bid = Bid(datetime(2023, 10, 1, 9, 0), david, asta2)

print(f"Utente di b0: {bid0.privato()()}")
print(f"Utente di b1: {bid1.privato()()}")
print(f"Utente di b3: {bid3.privato()()}")
print(f"Bid di anna: {[bid().bid() for bid in anna.bids()]}")

print()
print(f"Asta di b5: {bid5.asta()().descrizione()}")
print(f"Asta di b7: {bid7.asta()().descrizione()}")
print(f"Bid dell'asta1: {[bid().bid() for bid in asta1.bids()]}")
print(f"Bid dell'asta2: {[bid().bid() for bid in asta2.bids()]}")