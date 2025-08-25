# Try Except e finally -> Eccezioni

# Try: esegui un blocco di codice come test
# Except: permette di raccogliere l'errore e non far fermare il codice
# finally: esegue un altro codice una volta finito try except

x = 5
print(x)

try:
    print(y)                        # Y non esiste e dovrebbe dare errore terminando il codice
except NameError:
    print("Y non definita")         # dice che c'è un errore ma non mi blocca il codice
    pass                            # posso anche non fare niente
except ValueError:
    print("Se è un valueError")     # verrebbe stampato se il tipo di errore fosse corretto
else:
    print("Nessun problema")        # dato che non ci sono errori arriverà all'else

finally:
    print("finally")                # lo stamperà a prescindere


z = -1
if z < 0:
    raise ValueError("Numero minore di zero)")

print("ciao")