from persona import Persona
from studente import Studente

#crea una oggetto persona


p:Persona = Persona("Stefano","Reali",34)

#visualizzare le informazioni di persona
print(p)

#creare le informazioni della classe studente






studente:Studente = Studente("Mario", "Rossi", 33, "032656")

#voglio controllare che studente sia un istanza della classe studente
if isinstance(studente,Studente):
    print("studente1 è un oggetto della classe studente")

#la funzione isInstance ritorna True se effettivamente la studente1 è veramente un istanza della classe Studente

#voglio sapere se studente1 è un anche istanza della classe Persona

if isinstance(studente,Persona):
    print("L'oggetto studente è anche un istanza della classe Persona")

else:
    print("L'oggetto è solo un istanza della classe studente")


#voglio controllare che l'oggetto p sia un istanza di Persona

if isinstance(p,Persona):
    print("L'oggetto p è un istanza della classe Persona")
else:
    print("L'oggetto P non è un istanza della classe Persona")

#voglio controllare che l'oggetto p sia un istanza della classe Studente

if isinstance(p,Studente):
    print("L'oggetto è un istanza della classe Studenti")
else:
    print("L'oggetto non è un istanza della classe Studente")


#voglio controllare se studente è sottoclasse della classe Persona

if issubclass (Studente,Persona):
    print ("La classe Studente è  una sottoclasse di Persona")
else:
    print("La classe Studente non è sottoclasse della classe Persona")


#informazione sullo studente

print(studente)


print(p)



print(f" La media dei voti degli esami sostenuti dallo studente è : {studente.defGetMediaEsami([10,20,30])}")

#creiamo un nuovo studente

studente2:Studente = Studente(p.getName(),p.getCognome(),p.getEta(),"098762")
print(studente2)

#confrontare se studente è uguale a == p

print("\n", studente == p)

#confronto studente e studente2

print("\n", studente == studente2)

#verifichiamo che lo studente sia uguale a se stesso

print("\n", studente == studente)

#modificare nome e cognome ed età dello studente2 affinche abbia lo stesso nome, lo stesso cogno e la stessa età dello studente.

studente2.setName(studente.getName())
studente2.setCognome(studente.getCognome())
studente2.setEta(studente.getEta())

#riverifico che lo studente sia uguale a studente2 dopo aver modificato il nome, cognome, età rendendoli uguali
print("\n", studente == studente2)

#forzo la matricola ad essere uguale in entrambi
studente2.setMatricola(studente.getMatricola())


#verifico di nuovo il confronto
print("\n", studente == studente2)

print(studente.getMatricola())
print(studente2.getMatricola())

#richiamo metodo __call__
studente()
studente2()
p()

