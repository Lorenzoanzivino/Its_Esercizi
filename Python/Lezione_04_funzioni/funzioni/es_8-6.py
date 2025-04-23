'''8-6. Nomi della città: scrivi una funzione chiamata city-country() che prende il nome di una città e del suo paese. La funzione dovrebbe restituire una stringa formattata in questo modo: "Santiago, Cile". Chiama la tua funzione con almeno tre coppie di città-paese e stampa i valori che vengono restituiti.'''

def city_country(city:str,country:str):
    formatted:str = f"{city.capitalize()}, {country.capitalize()}"

    return formatted


print(city_country("roma","italia"))
print(city_country("los angeles", "california"))
print(city_country("stockholm", "sweden"))