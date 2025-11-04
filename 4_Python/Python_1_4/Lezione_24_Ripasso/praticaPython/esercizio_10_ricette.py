# 10
'''Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, e cercare ricette basate sugli ingredienti. Il sistema dovrà essere capace di gestire una collezione (dizionario) di ricette e i loro ingredienti.

Classe:
- RecipeManager:
    Gestisce tutte le operazioni legate alle ricette.

    Metodi:
    - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. Restituisce un nuovo dizionario con la sola ricetta appena creata o un messaggio di errore se la ricetta esiste già.

    - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.

    - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

    - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

    - list_recipes(): Elenca tutte le ricette esistenti.

    - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.

    - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.'''

class RecipeManager:
    
    def __init__(self):
        self.recipes = {}

    def create_recipe(self, name, ingredients):
        if name in self.recipes:
            return f"Errore: La ricetta '{name}' esiste già."
        
        self.recipes[name] = list(ingredients)
        return {name: self.recipes[name]}

    def add_ingredient(self, recipe_name, ingredient):
        if recipe_name not in self.recipes:
            return f"Errore: La ricetta '{recipe_name}' non esiste."
        
        if ingredient in self.recipes[recipe_name]:
            return f"Errore: L'ingrediente '{ingredient}' esiste già in '{recipe_name}'."
        
        self.recipes[recipe_name].append(ingredient)
        return {recipe_name: self.recipes[recipe_name]}

    def remove_ingredient(self, recipe_name, ingredient):
        if recipe_name not in self.recipes:
            return f"Errore: La ricetta '{recipe_name}' non esiste."
        
        if ingredient not in self.recipes[recipe_name]:
            return f"Errore: L'ingrediente '{ingredient}' non è presente in '{recipe_name}'."
        
        self.recipes[recipe_name].remove(ingredient)
        return {recipe_name: self.recipes[recipe_name]}

    def update_ingredient(self, recipe_name, old_ingredient, new_ingredient):
        if recipe_name not in self.recipes:
            return f"Errore: La ricetta '{recipe_name}' non esiste."
        
        if old_ingredient not in self.recipes[recipe_name]:
            return f"Errore: L'ingrediente '{old_ingredient}' non è presente in '{recipe_name}'."
        
        try:
            index = self.recipes[recipe_name].index(old_ingredient)
            self.recipes[recipe_name][index] = new_ingredient
            return {recipe_name: self.recipes[recipe_name]}
        except ValueError:
            return f"Errore: Ingrediente '{old_ingredient}' non trovato."

    def list_recipes(self):
        if not self.recipes:
            return "Nessuna ricetta nel ricettario."
        return list(self.recipes.keys())

    def list_ingredients(self, recipe_name):
        if recipe_name not in self.recipes:
            return f"Errore: La ricetta '{recipe_name}' non esiste."
        
        return self.recipes[recipe_name]

    def search_recipe_by_ingredient(self, ingredient):
        # Modifica chiave: deve restituire un dizionario di ricette, non una lista di nomi.
        found_recipes = {}
        for recipe_name, ingredients_list in self.recipes.items():
            if ingredient in ingredients_list:
                found_recipes[recipe_name] = ingredients_list
        
        if not found_recipes:
            return f"Errore: Nessuna ricetta trovata con l'ingrediente '{ingredient}'."
        
        return found_recipes


manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))
#{'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella']}
#{'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella', 'Basilico']}
#{'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']}
#{'Pizza Margherita': ['Farina', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']}
#['Farina', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']