'''4-5.
Somma di un milione: crea un elenco di numeri da uno a un milione, quindi usa min() e max() per assicurarti che l'elenco inizi effettivamente da uno e finisca da un milione. Inoltre, usa la funzione sum() per vedere quanto velocemente Python può aggiungere un milione di numeri.'''

milione:list[int] = []

for numero in range (1, 1000001):
    milione.append(numero)
print(milione)
print("Il minimo della lista è:", min(milione))
print("Il massimo della lista è:", max(milione))
print("La somma dei numeri da 1 a un milione è:", sum(milione))