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

# Creo i dottori (aggiungendo anche l'età nel costruttore)
dottore1 = Dottore("Lorenzo", "Anzivino", 32, "Pediatra", 100.99)
dottore2 = Dottore("Stefano", "Reali", 41, "Medico Generale", 120.99)

# Presentazione dei dottori
dottore1.doctor_greet()
dottore2.doctor_greet()

# Creo pazienti
paziente1 = Paziente("Mario", "Rossi", 28, "P001")
paziente2 = Paziente("Lucia", "Bianchi", 44, "P002")
paziente3 = Paziente("Giovanni", "Verdi", 13, "P003")
paziente4 = Paziente("Elena", "Neri", 56, "P004")

# Liste di pazienti
lista_pazienti1 = [paziente1, paziente2, paziente3]
lista_pazienti2 = [paziente4]

# Creo le fatture
fattura1 = Fattura(lista_pazienti1, dottore1)
fattura2 = Fattura(lista_pazienti2, dottore2)

# Stampo i salari iniziali
if fattura1.get_salary() is not None:
    print(f"\nSalario Dottore1: {fattura1.get_salary():.2f} euro!")
if fattura2.get_salary() is not None:
    print(f"Salario Dottore2: {fattura2.get_salary():.2f} euro!")

# Rimuovo un paziente dalla lista del dottore1 e lo aggiungo al dottore2
fattura1.remove_patient("P003")  # Giovanni Verdi
fattura2.add_patient(paziente3)

# Stampo i salari aggiornati
if fattura1.get_salary() is not None:
    print(f"\nSalario Dottore1 dopo modifica: {fattura1.get_salary():.2f} euro!")
if fattura2.get_salary() is not None:
    print(f"Salario Dottore2 dopo modifica: {fattura2.get_salary():.2f} euro!")

# Calcolo guadagno totale dell'ospedale
guadagno_totale = 0
if fattura1.get_salary() is not None:
    guadagno_totale += fattura1.get_salary()
if fattura2.get_salary() is not None:
    guadagno_totale += fattura2.get_salary()

print(f"\nIn totale, l'ospedale ha incassato: {guadagno_totale:.2f} euro!")
