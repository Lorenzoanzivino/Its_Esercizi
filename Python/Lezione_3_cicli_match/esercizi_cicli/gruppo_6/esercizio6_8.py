'''- 6-8. Animali: Fare diversi dizionari, dove ogni dizionario rappresenta un animale domestico diverso. In ogni dizionario, includere il tipo di animale e il nome del proprietario. Conservare questi dizionari in una lista chiamata animali domestici. Successivamente, passa attraverso la tua lista e come
Fai, stampa tutto quello che sai su ogni animale.'''

from typing import Any

dog_pet:dict[str, str] = {"animal": "dog", "owner's name": "Marcel"}
cat_pet:dict[str, str] = {"animal": "cat", "owner's name": "Stefano"}
lama_pet:dict[str, str] = {"animal": "lama", "owner's name": "Lorenzo"}

pets:list[str] = [dog_pet, cat_pet, lama_pet]

for animal in pets:
    print(animal)