from persona import Persona
from alieno import Alieno

# creare un oggetto p della Classe Persona
p: Persona = Persona("Lorenzo", "Anzivino", 27)

# visualizziamo le info della Persona p
print(p)

# creare un oggetto et della Classe Alieno
et: Alieno = Alieno("Andromeda")

# visualizza le info dell'allieno
print(et)

'''
POLIMORFISMO : molte-forme

- Usato su oggetti di classi diverse senza relazione tra loro
- Ma in entrambe le classi abbiamo il metodo speak()

'''
# oggetto p della classe Persona invoca il metodo speak()
p.speak()

# oggetto et della classe Alieno invoca il metodo speak()
et.speak()