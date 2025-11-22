'''Es 4 Scrivere un programma per creare una funzione show_employee() e Usare le seguenti condizioni.

    Dovrebbe accettare il nome e lo stipendio del dipendente e visualizzare entrambi.
    Se lo stipendio manca nella chiamata di funzione, assegnare il valore predefinito 9000 allo stipendio'''

def show_employee(nome:str, stipendio:float = 9000):
    print(f"Nome:, {nome}, Salario:, {stipendio}")

show_employee("Lorenzo", 3000)
show_employee("marco")
