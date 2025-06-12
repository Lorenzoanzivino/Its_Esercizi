from implementazione import *

alice: Studente = Studente('Alice')
biagio: Studente = Studente('Biagio')

prog1: Modulo = Modulo("Prog.1")
python14: Modulo = Modulo("Python.1-4")
web12: Modulo = Modulo("Web.1-2")

alice.add_esame(modulo=prog1, voto=28)
alice.add_esame(modulo=python14, voto=29)

alice.remove_esame(prog1)

try:
    alice.add_esame(modulo=python14, voto=31)
    print("Siamo riusciti ad aggiungere di nuovo un esame di Python.1-4 ad alice!")
except RuntimeError:
    print(f"Ci siamo accorti che {alice.nome()} ha già superato il modulo {python14.codice()}")

esami_alice = alice.esami()
print(f"{alice.nome()} ha superato {len(esami_alice)} esami")


alice.add_esame(modulo=web12, voto=19)

media_alice: float = alice.media_voti()
print(f"La media dei voti di Alice è {media_alice}")

try:
    python14.esami()
except AttributeError:
    print("Gli oggetti 'Modulo' non hanno un metodo 'esami()'")





esami: set[esame] = set()

esami.update(alice.esami())
esami.update(biagio.esami())
