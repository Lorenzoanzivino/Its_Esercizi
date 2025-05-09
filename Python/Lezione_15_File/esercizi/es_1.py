'''Crea un context manager usando una classe

Definisci una classe FileManager che implementa un context manager che gestisce le risorse dei file.

Implementa appropriatamente la funzione __init__, __enter__ e la funzione  __exit__

Esempio di funzionamento:

Il context manager deve permettere di aprire il file, effettuare operazioni e chiudere la risorsa aperta.

with FileManager('example.txt', 'w') as f:

    f.write('Hello, world!')'''

class FileManager:
    def __init__(self, file: str, mode: str, encoding="utf-8"):
        self.file = file
        self.wrapper = None
        self.mode = mode
        self.encoding = encoding

    def __enter__(self):
        self.wrapper = open(self.file, self.mode, encoding=self.encoding)
        print("Resource acquired")
        return self.wrapper  # restituisce direttamente l'oggetto file

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource released")
        self.wrapper.close()
        if exc_type is not None:
            print(f"An error occurred: {exc_type}")
            print(f"An error occurred: {exc_value}")
            print(f"An error occurred: {traceback}")
        return True  # sopprime eventuali eccezioni
    
with FileManager("example.txt", "w") as f:
    f.write("Hello, world!") 
    f.write("Ciao, sono Lorenzo ANzivino")

with FileManager("example.txt", "r") as f:
    print(f.read())

