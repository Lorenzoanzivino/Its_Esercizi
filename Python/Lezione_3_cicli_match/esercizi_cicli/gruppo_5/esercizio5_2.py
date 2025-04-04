'''5-2.
Altri test condizionali: non devi limitare il numero di test che crei a 10. Se vuoi provare più confronti, scrivi altri test e aggiungili
a conditional_tests.py. Avere almeno un risultato Vero e uno Falso per ciascuno dei seguenti:
• Test di uguaglianza e disuguaglianza con stringhe
• Test che utilizzano il metodo lower()
• Test numerici che coinvolgono uguaglianza e disuguaglianza, maggiore e minore, maggiore o uguale e minore o uguale
• Test che utilizzano la parola chiave and e la parola chiave or
• Testare se un elemento è in un elenco
• Testare se un elemento non è in un elenco'''

name:str = "Marcel"
print("Is name == 'Marcel'? I predict True.")
print(name == 'Marcel')
print("Is name == 'Stefano'? I predict False.")
print(name == 'Stefano')


name:str = "Marcel"
print("\nIs name == 'Marcel'? I predict True.")
print(name == 'Marcel')
print("Is name == 'marcel'? I predict False.")
print(name == 'Marcel'.lower)


number:int = 5
print("\nIs number > '4'? I predict True.")
print(number > 4)
print("Is number < '4'? I predict False.")
print(number < 4)


age1:int = 10
age2:int = 15
print("\nIs age1 or age2  > '4'? I predict True.")
print(age1 > 4 or age2 > 4)
print("Is age1 and age2 > '12'? I predict False.")
print(age1 > 12 and age2 > 12)


pizza_list:list[str] = ["Pizza Margherita", "Pizza ai Peperoni", "Pizza Diavola", "Pizza ai Funghi"]
print("\nIs Pizza Margherita in 'pizza_list'? I predict True.")
print("Pizza Margherita" in (pizza_list))
print("Focaccia in 'pizza_list'? I predict False.")
print("Focaccia" in (pizza_list))



