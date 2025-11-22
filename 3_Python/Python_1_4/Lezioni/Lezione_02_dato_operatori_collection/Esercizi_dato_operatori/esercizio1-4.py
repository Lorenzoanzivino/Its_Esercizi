''' 1-4
    Si scriva un programma che dato un intero di quattro cifre, per esempio 2024, utilizzando gli
    opportuni operatori, lo si visualizzi, una cifra per riga:'''


mylist= [2,0,2,5]

print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])


#1 Modo usando operatori 
n=int(input("inserisci un numero di 4 cifre:"))
m = n // 1000
c = n // 100 - m*10
d = n // 10 - m*100 - c*10
u = n - m*1000 - c*100 - d*10

print(m)
print(c)
print(d)
print(u)


#2 Modo con operatore modulo(%)
n:int = 2024 

# stampare a schermo le migliaia.
# Poichè la divisione da come risultato un numero float, 
# devo convertire il risultato della divisione in un numero intero, usando la funzione int()
print(int(n/1000)) # 2024/1000=2

# numero da valutare per le centinaia, decine ed unità
n=n%1000 # n = 2024%1000=24 

# stamapre a schermo le centinaia
print(int(n/100)) # 24/100=0

# numero da valutare per le decine e le unità
n=n%100 # n = 24%100 = 24 

# stampare a schermo le decine 
print(int(n/10)) # 24/10=2 

# numero da valutare per le unità 
n=n%10 # n = 24%10=4 

# stampare a schermo le unità

print(int(n/1))
# la divisione n/1 darà sempre resto 0, quindi abbiamo finito il nostro procedimento.
# pertanto non è necessario valutare n%1