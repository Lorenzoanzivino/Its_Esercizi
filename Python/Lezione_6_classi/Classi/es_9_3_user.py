'''9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users, and call both methods for each user.'''


class User:
    def __init__(self, first_name: str, last_name: str, age: int, gender: str):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):

        print(f'nome: {self.first_name} - cognome: {self.last_name} - anni {self.age} - Genere: {self.gender}')


lorenzo: User = User("Lorenzo", "Anzivino", 28, "Male")
stefano: User = User("Stefano", "Reali", 34, "Male")
leandro: User = User("Leandro", "Pazienza", 27, "Male")
francesco: User = User("Francesco", "Magno", 12, "Male")

lorenzo.describe_user()
stefano.describe_user()
leandro.describe_user()
francesco.describe_user()