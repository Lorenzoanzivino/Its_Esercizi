'''6-12. Estensioni: stiamo lavorando con esempi abbastanza complessi da poter essere estesi in qualsiasi modo. Usa uno dei programmi di esempio di questo capitolo ed estensilo aggiungendo nuove chiavi e valori, modificando il contesto del programma o migliorando la formattazione dell'output.'''

from typing import Any

citta:dict[str, Any] = {"Rome":{"Country": "Italy", "Population": "2.76 million", "Fact": "Has 280 fountains and more than 900 churches"},"Okinawa":{"Country": "Japan","Population": "1.47 million", "Fact": "It's 2,271 square km big"},"Hollywood":{"Country": "America", "Population": "70,915", "Fact": "It's the center of the American film industry"}}
for key, value in citta.items():
    for place in value:
        print(f"{key}: Country - {citta[key]['Country']} | Population - {citta[key]['Population']} | Fact - {citta[key]['Fact']}")
        break
        