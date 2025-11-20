'''9-10. Ristorante Importato: Usando la tua ultima classe Restaurant, memorizzala in un modulo. Crea un file separato che importa Restaurant. Crea un'istanza di Restaurant e chiama uno dei metodi di Restaurant per verificare che l'istruzione di importazione funzioni correttamente.'''

from es_9_4_clienti import Restaurant

# Crea un'istanza di Restaurant
restaurant = Restaurant("La Trattoria", "Italiana")

# Chiama uno dei metodi della classe Restaurant
restaurant.describe_restaurant()
restaurant.open_restaurant()