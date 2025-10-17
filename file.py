lista:list = [-1,-2,-3, 5, 5, 2]
lista_nuova= []
somma = 0
for n in lista:
    if n > 0:
        lista_nuova.append(n)
        somma += n
        media = somma // len (lista_nuova)

print(lista_nuova)
print(somma)
print(media)
