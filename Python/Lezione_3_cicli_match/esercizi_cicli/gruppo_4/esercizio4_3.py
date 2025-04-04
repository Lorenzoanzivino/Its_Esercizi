'''4-3. Contare fino a venti: utilizzare un ciclo for per stampare i numeri da 1 a 20, inclusi.'''

for numeri in range(1, 21):
    #cosi stampo i numeri in fila creando uno spazio, ma dopo 21 si crea uno spazio in più e viene occupato in automatico da "%"
    print(numeri, end=", ") 
    #in questo modo elimino il problema di "%"
    print(", ".join(str(i) for i in range(1, 21)))