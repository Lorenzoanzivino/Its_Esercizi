from implementazione import *
import sys

alice: Studente = Studente("Alice")
biagio:Studente = Studente("biagio")

prog1:Modulo = Modulo("Prog.1")
python14:Modulo = Modulo("Python1-4")

alice.add_esame(modulo=prog1, voto=28)
alice.add_esame(modulo=python14, voto=29)

alice.remove_esame(prog1)

try:
    alice.add_esame(modulo=python14, voto=31)
except RuntimeError:
    print(f"{alice.nome()} ha già superato l'esame del modulo python14")

esami_alice = alice.esami()
print(f"{alice.nome()} ha superato {len(esami_alice)} esami")

media_alice: float = esami_alice.media_voti()

try:
    python14.esami()
except:
    print("Gli oggetti 'modulo' non hanno metodo 'esami'")