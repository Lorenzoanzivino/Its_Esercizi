
'''3-6.
More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.'''

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
#invitati_cena.insert(3, "Fabio")

meta = len(invitati_cena)//2
invitati_cena.insert(meta, "Fabio")

invitati_cena.append("Carlo")
print(invitati_cena)

for invitato in invitati_cena:
    print(f"Ciao,{invitato}, sei invitato alla mia cena")