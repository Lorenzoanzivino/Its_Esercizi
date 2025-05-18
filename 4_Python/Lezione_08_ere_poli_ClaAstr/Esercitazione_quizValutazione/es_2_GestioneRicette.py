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

    - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.

For example:
'''

class RecipeManager:
    def __init__(self):
        self.recipes = {}

    def create_recipe(self, name, ingredients):
        if name in self.recipes:
            return f"Errore: La ricetta '{name}' esiste già."
        unique_ingredients = list(dict.fromkeys(ingredients))
        self.recipes[name] = unique_ingredients
        return {name: self.recipes[name]}

    def add_ingredient(self, recipe_name, ingredient):
        if recipe_name not in self.recipes:
            return f"Errore: La ricetta '{recipe_name}' non esiste."
        if ingredient in self.recipes[recipe_name]:
            return f"Errore: L'ingrediente '{ingredient}' è già presente nella ricetta '{recipe_name}'."
        self.recipes[recipe_name].append(ingredient)
        return {recipe_name: self.recipes[recipe_name]}

    def remove_ingredient(self, recipe_name, ingredient):
        if recipe_name not in self.recipes:
            return f"Errore: La ricetta '{recipe_name}' non esiste."
        if ingredient not in self.recipes[recipe_name]:
            return f"Errore: L'ingrediente '{ingredient}' non è presente nella ricetta '{recipe_name}'."
        self.recipes[recipe_name].remove(ingredient)
        return {recipe_name: self.recipes[recipe_name]}

    def update_ingredient(self, recipe_name, old_ingredient, new_ingredient):
        if recipe_name not in self.recipes:
            return f"Errore: La ricetta '{recipe_name}' non esiste."
        if old_ingredient not in self.recipes[recipe_name]:
            return f"Errore: L'ingrediente '{old_ingredient}' non è presente nella ricetta '{recipe_name}'."
        if new_ingredient in self.recipes[recipe_name]:
            return f"Errore: L'ingrediente '{new_ingredient}' è già presente nella ricetta '{recipe_name}'."
        index = self.recipes[recipe_name].index(old_ingredient)
        self.recipes[recipe_name][index] = new_ingredient
        return {recipe_name: self.recipes[recipe_name]}

    def list_recipes(self):
        return list(self.recipes.keys()) if self.recipes else []

    def list_ingredients(self, recipe_name):
        if recipe_name not in self.recipes:
            return f"Errore: La ricetta '{recipe_name}' non esiste."
        return self.recipes[recipe_name]

    def search_recipe_by_ingredient(self, ingredient):
        found = [name for name, ingredients in self.recipes.items() if ingredient in ingredients]
        if not found:
            return f"Nessuna ricetta contiene l'ingrediente '{ingredient}'."
        return found
