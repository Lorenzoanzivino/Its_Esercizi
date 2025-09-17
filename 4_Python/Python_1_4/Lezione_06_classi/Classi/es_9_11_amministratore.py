'''9-11. Amministratore Importato: Crea un modulo users.py contenente tre classi:

    User: memorizza first_name, last_name, username e email; include i metodi describe_user() e greet_user().

    Privileges: contiene una lista di privilegi e un metodo show_privileges() per visualizzarli.

    Admin: memorizza un'istanza della classe User e un'istanza della classe Privileges come attributi.

In un file separato main.py, importa le classi, crea un'istanza di User e un'istanza di Privileges, passale a Admin e chiama describe_user() e show_privileges() per verificare che tutto funzioni correttamente.'''


class User:
    def __init__(self, first_name:str, last_name:str, username:str, email:str):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
    
    # descrizione dell'user
    def describe_user(self):
        print(f"Utente: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

    # dare il benvenuto all'utente
    def greet_user(self):
        print(f"Benvenuto, {self.first_name}!")

class Privileges:
    def __init__(self, privilegi:list):
        self.privilegi = privilegi

    def show_privileges(self):
        print(f"Privilegi: {self.privilegi}")


class Admin:
    def __init__(self, user:User, privilegi:Privileges):
        self.user = user
        self.privilegi = privilegi

    def show_info(self):
        self.user.describe_user()
        self.privilegi.show_privileges()

