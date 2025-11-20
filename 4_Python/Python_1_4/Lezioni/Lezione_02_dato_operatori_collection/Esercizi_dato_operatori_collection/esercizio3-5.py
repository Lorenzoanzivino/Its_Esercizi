'''3-5.
Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.'''

invitati_cena:list[str] = ["Stefano", "Veronica", "Francesco", "Marco"]
print(invitati_cena)

for invitato in invitati_cena:
    print(f"Ciao,{invitato}, sei invitato alla mia cena")
    
print(f"Mi dispiace che non puoi venire, {invitati_cena[0]}")

invitati_cena[0] = "Simone"
print(invitati_cena)
print(f"Ciao {invitati_cena[0]}, sei invitato alla mia cena")