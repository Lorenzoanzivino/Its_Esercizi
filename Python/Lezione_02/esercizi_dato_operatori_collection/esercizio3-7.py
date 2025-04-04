'''3-7.
Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.'''

invitati_cena:list[str] = ["Stefano", "Veronica", "Francesco", "Marco"]
print(invitati_cena)

for invitato in invitati_cena:
    print(f"Ciao,{invitato}, sei invitato alla mia cena")
    
print(f"Mi dispiace che non puoi venire, {invitati_cena[0]}")

invitati_cena[0] = "Simone"
print(invitati_cena)
print(f"Ciao {invitati_cena[0]}, sei invitato alla mia cena")
print(f"{invitati_cena} ho trovato un tavolo più grande, si uniranno altre persone")

invitati_cena.insert(0, "Ciro")
meta = len(invitati_cena)//2
invitati_cena.insert(meta, "Fabio")
invitati_cena.append("Carlo")
print(invitati_cena)

for invitato in invitati_cena:
    print(f"Ciao,{invitato}, sei invitato alla mia cena")
print(f"Mi dispiace, {invitati_cena} ma non ho spazio per tutti")

while len(invitati_cena) > 2:
    ospite = invitati_cena.pop()  # Rimuove l'ultimo elemento dalla lista
    print(f"Mi dispiace {ospite}, non posso invitarti a cena.")  # Messaggio per l'ospite rimosso

# Alla fine della rimozione, stampa la lista finale con gli ultimi due invitati_cena
print("Gli invitati alla cena rimasti sono:", invitati_cena)
print(f"{invitati_cena}, siete invitati alla cena")

del invitati_cena[:]
print(invitati_cena)