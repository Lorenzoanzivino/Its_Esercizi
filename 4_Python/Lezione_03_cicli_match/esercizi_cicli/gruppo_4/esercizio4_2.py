'''4-2.
Animali: pensa ad almeno tre animali diversi che hanno una caratteristica comune. Memorizza i nomi di questi animali in un elenco, quindi usa un ciclo for per stampare il nome di ogni animale.
• Modifica il tuo programma per stampare una dichiarazione su ogni animale, come Un cane sarebbe un ottimo animale domestico.
• Aggiungi una riga alla fine del tuo programma, dichiarando cosa hanno in comune questi animali. Potresti stampare una frase, come Uno qualsiasi di questi animali sarebbe un ottimo animale domestico!'''

lista_animali:list[str] = ["Cane", "Cavallo", "Gatto"]
for animale in lista_animali:
    if animale == "Cane" or animale == "Gatto":
        print(f"Un {animale} sarebbe un ottimo animale domestico")
    elif animale == "Cavallo":
        print(f"Non credo che un {animale} possa essere domestico")

print(f'{", ".join(lista_animali)} hanno in comune: 4 zampe e sono mammiferi')