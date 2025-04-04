'''4-4.
Un milione: crea un elenco di numeri da uno a un milione, quindi usa un ciclo for per stampare i numeri. (Se l'output impiega troppo tempo, fermalo premendo CTRL-C o chiudendo la finestra di output.)'''

milione:list[int] = []

for numero in range (1, 1000001):
    milione.append(numero)
print(milione)