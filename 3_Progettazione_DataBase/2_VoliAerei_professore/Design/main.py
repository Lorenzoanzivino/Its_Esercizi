from classi import *
from custom_types import *

italia: Nazione = Nazione("Italia")
print(italia)
roma: Citta = Citta(nome="Roma", abitanti=IntGEZ(58), nazione=italia)

milano: Citta = Citta(nome="Milano", abitanti=IntGEZ(47), nazione=italia)
print(roma)
print(milano)

print(f"Città in italia: {[c.nome() for c in italia.citta()]}\n")
# deve contenere roma e milano


francia: Nazione = Nazione("Francia", citta={roma})


print(f"Città in italia: {[c.nome() for c in italia.citta()]}")
# deve contenere solo milano
print(f"Città in francia: {[c.nome() for c in francia.citta()]}\n\n")
# deve contenere solo roma





wizard_air: Compagnia = Compagnia(nome="Wizard Air",
                                  fondazione=IntGE1900(1988),
                                  citta=roma)

print(wizard_air)

fco: Aeroporto = Aeroporto(codice=CodiceIATA("FCO"),
                           nome="Aeroporto internazionale Leonardo da Vinci")

print(fco)


v1: Volo = Volo(codice=CodiceVolo("W46061"), durata=IntGZ(105), compagnia=wizard_air)
v2: Volo = Volo(codice=CodiceVolo("VY7375"), durata=IntGZ(125), compagnia=wizard_air)


print(v1)
print(v2)

print(f"Voli di Wizard Air: {wizard_air.voli()}")

welling: Compagnia = Compagnia(nome="Welling", fondazione=IntGE1900(1999),citta=milano)

welling._add_volo(v2) # c'è l'underscore davanti: non dovrei farlo!
print(f"Voli di Welling: {welling.voli()}")

wizard_air.remove_volo(v1)
print(f"Voli di Wizard Air: {wizard_air.voli()}")

print(v1)





