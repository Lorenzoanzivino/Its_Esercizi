'''Es 2 Scrivere un programma per creare funzione func1()Accettare una lunghezza variabile degli argomenti e stamparne il valore.

Nota : Creare una funzione in modo tale da poter passare qualsiasi numero di argomenti a questa funzione, e la funzione dovrebbe elaborarli e visualizzare il valore di ciascun argomento'''

def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)