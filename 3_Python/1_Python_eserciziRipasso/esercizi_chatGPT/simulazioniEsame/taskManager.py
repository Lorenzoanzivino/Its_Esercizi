'''Classe TaskManager — PUNTI 2

Progetta una classe TaskManager per gestire un elenco di attività (task).

Attributi

tasks: dict[str, dict]
Dizionario dove la chiave è un task_id (stringa) e il valore è un dizionario con:

"descrizione": str — descrizione del compito

"completato": bool — indica se il compito è completato o meno

Metodi

add_task(task_id: str, descrizione: str) -> dict | str
Se task_id esiste già, restituisce "Errore: task già esistente."
Altrimenti aggiunge un nuovo task con completato=False e restituisce il dizionario del nuovo task.

complete_task(task_id: str) -> dict | str
Se il task non esiste, restituisce "Errore: task non trovato."
Altrimenti imposta "completato" = True e restituisce il dizionario aggiornato.

delete_task(task_id: str) -> dict | str
Se non esiste, restituisce "Errore: task non trovato."
Altrimenti rimuove il task e restituisce il task rimosso.

list_incomplete() -> list[str]
Restituisce una lista con gli ID dei task non completati.

get_task(task_id: str) -> dict | str
Restituisce il dizionario del task, oppure "Errore: task non trovato."'''

class TaskManager:
    def __init__(self) -> None:
        self.tasks: dict[str, dict] = {}

    def add_task(self, task_id: str, descrizione: str) -> dict | str:
        if task_id in self.tasks:
            return "Errore: task già esistente."
        self.tasks[task_id] = {"descrizione": descrizione, "completato": False}
        return self.tasks[task_id]

    def complete_task(self, task_id: str) -> dict | str:
        if task_id not in self.tasks:
            return "Errore: task non trovato."
        self.tasks[task_id]["completato"] = True
        return self.tasks[task_id]

    def delete_task(self, task_id: str) -> dict | str:
        if task_id not in self.tasks:
            return "Errore: task non trovato."
        return self.tasks.pop(task_id)

    def list_incomplete(self) -> list[str]:
        incompleti = []
        for task_id, task in self.tasks.items():
            if not task["completato"]:
                incompleti.append(task_id)
        return incompleti

    def get_task(self, task_id: str) -> dict | str:
        if task_id not in self.tasks:
            return "Errore: task non trovato."
        return self.tasks[task_id]

# ==========================
# DRIVER COMPLETO
# ==========================
tm = TaskManager()

# aggiungo un task
print("Add:", tm.add_task("Lorenzo", "Studiare Python"))

# provo ad aggiungere lo stesso task (errore)
print("Add duplicato:", tm.add_task("Lorenzo", "Studiare Python"))

# controllo task
print("Get:", tm.get_task("Lorenzo"))

# lista incompleti prima di completare
print("Incompleti:", tm.list_incomplete())

# completo il task
print("Complete:", tm.complete_task("Lorenzo"))

# lista incompleti dopo aver completato
print("Incompleti:", tm.list_incomplete())

# cancello il task
print("Delete:", tm.delete_task("Lorenzo"))

# provo a cancellare di nuovo (errore)
print("Delete non esistente:", tm.delete_task("Lorenzo"))


