'''### Codice Driver

Scrivere, infine, il codice driver che gestisca due dottori e due liste di pazienti. La prima lista di pazienti deve contenere 3 pazienti, mentre la seconda 1 solo paziente.

    Impostare l'età di ogni medico, affinché i due medici risultino validi!
    Il primo medico e il secondo medico si presentano, richiamando il rispettivo metodo doctorGreet().
    Creare un oggetto fattura chiamato fattura1. Alla fattura 1 devono essere associati il dottore_1 e la lista di 3 pazienti.
    Creare un oggetto fattura chiamato fattura2. Alla fattura 2 devono essere associati il dottore_2 e la lista di un solo paziente.
    Stampare in output il salario di ogni singolo dottore. Ad esempio:

      "Salario Dottore1: ... euro!
       Salario Dottore2: ... euro!"

    Rimuovere un paziente dalla lista dei pazienti del dottore 1 ed inserire tale paziente nella lista del dottore 2.
    Stampare in output il salario di ogni dottore.
    Stampare in output il guadagno totale incassato dall'ospedale. Il guadagno totale viene calcolato sommando i guadagni di ogni dottore. Esempio:

"In totale, l'ospedale ha incassato: tot euro!"'''

from classe_dottore import Dottore
from classe_paziente import Paziente
from classe_fattura import Fattura

# Creo i dottori
dottore1 = Dottore("Lorenzo", "Anzivino", "Pediatra", 100.99)
dottore2 = Dottore("Stefano", "Reali", "Medico Generale", 120.00)

# Imposto età per renderli validi
dottore1.setAge(32)
dottore2.setAge(41)

# Presentazione dei dottori
dottore1.doctorGreet()
dottore2.doctorGreet()

# Creo pazienti
paziente1 = Paziente("Mario", "Rossi", "P001")
paziente2 = Paziente("Lucia", "Bianchi", "P002")
paziente3 = Paziente("Giovanni", "Verdi", "P003")
paziente4 = Paziente("Elena", "Neri", "P004")
paziente5 = Paziente("Alessandro", "Gallo", "P005")  # opzionale

# Liste di pazienti
lista_pazienti1 = [paziente1, paziente2, paziente3]
lista_pazienti2 = [paziente4]

# Creo le fatture
fattura1 = Fattura(lista_pazienti1, dottore1)
fattura2 = Fattura(lista_pazienti2, dottore2)

# Stampo i salari iniziali
print(f"\nSalario Dottore1: {fattura1.getSalary()} euro!")
print(f"Salario Dottore2: {fattura2.getSalary()} euro!")

# Rimuovo un paziente da fattura1 e lo aggiungo a fattura2
fattura1.removePatient("P003")  # Giovanni Verdi
fattura2.addPatient(paziente3)

# Stampo i salari aggiornati
print(f"\nSalario Dottore1 dopo modifica: {fattura1.getSalary()} euro!")
print(f"Salario Dottore2 dopo modifica: {fattura2.getSalary()} euro!")

# Calcolo guadagno totale dell'ospedale
guadagno_totale = fattura1.getSalary() + fattura2.getSalary()
print(f"\nIn totale, l'ospedale ha incassato: {guadagno_totale} euro!")
