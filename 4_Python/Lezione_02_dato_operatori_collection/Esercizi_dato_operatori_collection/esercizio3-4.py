'''3-4.
Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.'''

invitati_cena:list[str] = ["Stefano", "Veronica", "Francesco", "Marco"]
for invitato in invitati_cena:
    print(f"Ciao,{invitato}, sei invitato alla mia cena")