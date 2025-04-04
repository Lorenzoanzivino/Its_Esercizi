'''Tentativi di accesso 9-5. 
- Aggiungi un attributo chiamato login_attempts alla tua classe User dell'esercizio 9-3. 
- Scrivi un metodo chiamato increment_login_attempts() che incrementa il valore di login_attempts di 1. 
- Scrivi un altro metodo chiamato reset_login_attempts() che reimposta il valore di login_attempts a 0. 
- Crea un'istanza della classe User e chiama increment_login_attempts() più volte. 
- Stampa il valore di login_attempts per assicurarti che sia stato incrementato correttamente, quindi chiama reset_login_attempts(). 
- Stampa di nuovo login_attempts per assicurarti che sia stato reimpostato a 0.'''

class User:
    def __init__(self, first_name: str, last_name: str, age: int, gender: str, login_attempts: int = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f'nome: {self.first_name} - cognome: {self.last_name} - anni: {self.age} - Genere: {self.gender}')

    def increment_login_attempts(self):
        self.login_attempts += 1  # Aumenta di 1 il numero dei tentativi di accesso

    def reset_login_attempts(self):
        self.login_attempts = 0  # Resetta il numero dei tentativi di accesso

# Creiamo correttamente le istanze della classe User
lorenzo = User("Lorenzo", "Anzivino", 28, "Male", 0)
stefano = User("Stefano", "Reali", 34, "Male", 0)
leandro = User("Leandro", "Pazienza", 27, "Male", 0)
francesco = User("Francesco", "Magno", 12, "Male", 0)

# Descrizione degli utenti
lorenzo.describe_user()
stefano.describe_user()
leandro.describe_user()
francesco.describe_user()

# Incremento i tentativi di accesso per Lorenzo
lorenzo.increment_login_attempts()
lorenzo.increment_login_attempts()
lorenzo.increment_login_attempts()

# Stampa del numero di tentativi di accesso di Lorenzo
print(f"\nNumero tentativi di accesso di Lorenzo dopo gli incrementi: {lorenzo.login_attempts}")

# Resettiamo i tentativi di accesso
lorenzo.reset_login_attempts()

# Stampa del numero di tentativi di accesso dopo il reset
print(f"Numero tentativi di accesso di Lorenzo dopo il reset: {lorenzo.login_attempts}")
