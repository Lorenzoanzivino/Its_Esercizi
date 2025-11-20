'''Esercizio 3C-6.
Modificare il codice dell'esercizio 3C-4, affinchè si possa scrivere un codice python che consenta all'utente di inserire il nome di un animale ed un habitat. Quando il codice dell'esercizo 3C-4 classifica l'animale inserito in una delle categorie tra mammiferi, rettili, uccelli o pesci, oltre a mostrare un messaggio a schermo, deve salvare tale categoria in una variabile animal_type. Se l'animale inserito non è classificabile in una delle quattro categorie proposte, il valore di animal_type sarà ' "unknown".

Inserire, poi, in un dizionario il nome dell'animale, la categoria a cui esso appartiene (animal_type) e l'habitat.

Verificare con un match statement se l'animale e la categoria a cui esso appartiene possano vivere nell'habitat inserito; dunque, verificare:
- se l'animale può vivere nell'habitat specificato, stampare un messaggio appropriato.
- se l'habitat non è compatibile con l'habitat specificato, stampare un avviso.
- Se l'animale o l'habitat non sono riconosciuti, stampare un messaggio di errore.

Le categorie di classificazione devono essere:
- Mammiferi: cane, gatto, cavallo, elefante, leone, balena, delfino.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco, cigno, anatra, gallina, tacchino.
- Pesci: squalo, trota, salmone, carpa.
Categorie di habitat:
- acqua
- aria
- terra
NOTA.
Il codice deve produrre un risultato sensato, ovvero che l'animale inserito possa effettivamente vivere nell'habitat specificato.
Tenere in considerazione il fatto che alcuni animali tra quelli specificati possono vivere in più di un habitat, mentre altri solo in uno.
Suggeirmento: può essere utile per coprire tutti i possibili casi implementare istruzioni match annidate.'''


# Input utente
animal:str = str(input("Digita il nome di un animale: "))
habitat:str = str(input(f"Digita l'habitat in cui vive l'animale {animal}: "))
animal_type: str

match animal:
    case ("cane"|"gatto"|"cavallo"|"elefante"|"leone"|"balena"|"delfino"):
        print(f"{animal} appartiene alla categoria dei mammiferi")
        animal_type = "mammiferi"
    case ("serpente"|"lucertola"|"tartaruga"|"coccodrillo"):
        print(f"{animal} appartiene alla categoria dei rettili")
        animal_type = "rettili"
    case ("aquila"|"pappagallo"|"gufo"|"falco"|"cigno"|"anatra"|"gallina"|"tacchino"):
        print(f"{animal} appartiene alla categoria degli uccelli")
        animal_type = "uccelli"
    case ("squalo"|"trota"|"salmone"|"carpa"):
        print(f"{animal} appartiene alla categoria dei pesci")
        animal_type = "pesci"
    case _:
        print(f"Non so dire in quale categoria classificare l'animale {animal}")
        print(f"Non sono in grado di fornire informazioni sull'habitat {habitat}")
        animal_type = "unknown"

# modo alternativo per scrivere il dizionario
dizionario = dict(name=animal, habitat=habitat, tipo=animal_type)

match animal_type:
    case "mammiferi":
        match habitat:
            case habitat if habitat == "terra" and animal in ["cane", "gatto", "cavallo", "elefante", "leone"]:
                print(f"{animal} è uno dei {animal_type} che può vivere in {habitat}") 
            case habitat if habitat == "acqua" and animal in ["balena", "delfino"]:
                print(f"{animal} è uno dei {animal_type} che può vivere in {habitat}")
            case _:
                print(f"Non ho mai visto {animal} vivere nell'habitat {habitat}")
            
    case "rettili":
        match habitat:
            case habitat if habitat == "terra" and animal in ["serpente", "lucertola", "tartaruga", "coccodrillo"]:
                print(f"{animal} è uno dei {animal_type} che può vivere in {habitat}")
            case habitat if habitat == "acqua" and animal in ["tartaruga", "coccodrillo"]:
                print(f"{animal} è uno dei {animal_type} che può vivere in {habitat}")
            case _:
                print(f"Non ho mai visto {animal} vivere nell'habitat {habitat}")

    case "uccelli":
        match habitat:
            case habitat if habitat == "aria" and animal in ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra"]:
                print(f"{animal} è uno dei {animal_type} che può vivere in {habitat}")
            case habitat if habitat == "terra" and animal in ["gallina", "tacchino"]:
                print(f"{animal} è uno dei {animal_type} che può vivere in {habitat}")
            case _:
                print(f"Non ho mai visto {animal} vivere nell'habitat {habitat}")
    
    case "pesci":
        match habitat:
            case habitat if habitat == "acqua" and animal in ["squalo", "trota", "salmone", "carpa"]:
                print(f"{animal} è uno dei {animal_type} che può vivere in {habitat}")
            case _:
                print(f"Non ho mai visto {animal} vivere nell'habitat {habitat}")