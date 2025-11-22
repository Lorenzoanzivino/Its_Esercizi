'''9-11. Amministratore Importato: Crea un modulo users.py contenente tre classi:

    User: memorizza first_name, last_name, username e email; include i metodi describe_user() e greet_user().

    Privileges: contiene una lista di privilegi e un metodo show_privileges() per visualizzarli.

    Admin: memorizza un'istanza della classe User e un'istanza della classe Privileges come attributi.

In un file separato main.py, importa le classi, crea un'istanza di User e un'istanza di Privileges, passale a Admin e chiama describe_user() e show_privileges() per verificare che tutto funzioni correttamente.'''


from es_9_11_amministratore import *

la:User = User("Lorenzo", "Anzivino", "Lollo97", "lorenzo@ciao.com")
privilegi:Privileges = Privileges(["amministratore", "bla bla"])

admin:Admin = Admin(la, privilegi)

admin.show_info()