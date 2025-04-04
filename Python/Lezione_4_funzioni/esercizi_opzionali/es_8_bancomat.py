''' 8. Simulatore di Bancomat: 
Crea una funzione che simuli un bancomat.
Inizializza un conto con un saldo iniziale.
Consenti all'utente di eseguire transazioni come deposito, prelievo e verifica del saldo.
Valida le transazioni contro il saldo del conto e i fondi disponibili.
Fornisci un feedback appropriato all'utente per ogni transazione.'''

def deposito(saldo:float, importo:float) -> float:
    saldo += importo 
    return saldo

def prelievo(saldo:float, importo:float) -> float:
    if importo <= saldo:
        saldo -= importo
        return saldo
    else:
        print("Fondi insufficienti!")
        return saldo
    
def visualizza_saldo(saldo:float) -> None:
    print(f"Il saldo attuale è: {saldo:.2f}")

def scegli_operazione() -> str:
    print("\nScegli un'operazione:")
    print("1 - Deposito denaro")
    print("2 - Prelievo denaro")
    print("3 - Visualizza saldo")
    print("4 - Esci")

    scelta = input("\nScegli la tua operazione: ")
    return scelta

def bancomat():
    saldo:float = 15000
    while True:
        scelta = scegli_operazione()

        if scelta == "1":
            aggiungi:float = float(input("Quanto vuoi depositare? "))
            if aggiungi < 0:
                print("L'importo del deposito non può essere negativo.")
            else:
                saldo = deposito(saldo, aggiungi)
                print(f"Il tuo saldo attuale è: {saldo:.2f}")
                
        
        elif scelta == "2":
            ritira:float = float(input("Quanto vuoi prelevare? "))
            if ritira < 0:
                print("L'importo del prelievo non può essere negativo.")
            elif ritira > saldo:
                print("Non possiedi abbastanza fondi per prelevare.")
            else:
                saldo = prelievo(saldo, ritira)
                print(f"Il tuo saldo attuale è € {saldo:.2f}")

        elif scelta == "3":
                visualizza_saldo(saldo)
        elif scelta == "4":
            print("Uscendo dal programma.")
            break
        else:
            print("Operazione non valida. Riprova.")

bancomat()