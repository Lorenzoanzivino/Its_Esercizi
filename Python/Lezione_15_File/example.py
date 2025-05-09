# Funzione open()

# PATH: str = "example.txt"
# file = open(PATH, "r", encoding="utf-8")
# output: str = file.read()
# print(output)

file = open("example.txt", "a")
try :
    pass
except Exception as e:
    pass
finally :
    file.close()

# CONTEXT : (context manager = classe che ha __enter__() / __exit__())
# Uscendo dal print che è indentato il file si chiude automaticamente# il WITH sostituisce la creazione del percorso di un file scritto sopra
with open("example.txt", "w") as file :
    print(file.read())


# Spiegazione di come funziona il WITH gestisce tutto in automatico tramite questa classe
class MyResource :
    def __enter(self) :
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Sono nella funzione")

        if exc_type is not None:
            print(f"An error occured: {exc_value}")

        return True
    
print("iNIZIO DEL PROGRAMMA")

with MyResource() as resources :
    print("Sono dentro il blocco with")


import json

with open("config.json", "r") as file:
    
    my_config : dict = json.load(file)

    print(my_config["name"])