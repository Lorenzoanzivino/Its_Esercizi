'''es 7.Eccezione Personalizzata per l'Integrità delle Strutture Dati

Definisci una classe di eccezione personalizzata DataStructureIntegrityError.

Implementa una struttura dati lista collegata (linked list) con i seguenti metodi:

    Aggiungere (append)

    Rimuovere (remove)

    Accedere a un elemento specifico

Scrivi funzioni per:

    Stampare la lista

    Invertire la lista

    Verificare se la lista è ordinata

Solleva l'eccezione DataStructureIntegrityError se l'integrità della struttura dati viene compromessa (ad esempio, accesso a una lista vuota o errore di indice).'''

class DataStructureIntegrityError(Exception):
    pass

class Nodo:
    def __init__(self, valore):
        self.valore = valore
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, valore):
        nuovo_nodo = Nodo(valore)
        if not self.head:
            self.head = nuovo_nodo
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = nuovo_nodo
    
    def remove(self, valore):
        if not self.head:
            raise DataStructureIntegrityError("Rimozione da lista vuota.")
        
        # Rimuove la prima occorrenza di valore
        if self.head.valore == valore:
            self.head = self.head.next
            return
        
        prev = self.head
        current = self.head.next
        while current:
            if current.valore == valore:
                prev.next = current.next
                return
            prev = current
            current = current.next
        
        raise DataStructureIntegrityError(f"Valore {valore} non trovato nella lista.")
    
    def get(self, index):
        if not self.head:
            raise DataStructureIntegrityError("Accesso a lista vuota.")
        if index < 0:
            raise DataStructureIntegrityError("Indice negativo non valido.")
        
        current = self.head
        cont = 0
        while current:
            if cont == index:
                return current.valore
            current = current.next
            cont += 1
        
        raise DataStructureIntegrityError("Indice fuori intervallo.")
    
    def stampa(self):
        valori = []
        current = self.head
        while current:
            valori.append(str(current.valore))
            current = current.next
        print(" -> ".join(valori))
    
    def inverti(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev
    
    def is_ordinata(self):
        if not self.head or not self.head.next:
            return True  # Lista vuota o con un solo elemento è ordinata
        current = self.head
        while current.next:
            if current.valore > current.next.valore:
                return False
            current = current.next
        return True


# Esempio di utilizzo

try:
    lista = LinkedList()
    lista.append(3)
    lista.append(5)
    lista.append(2)
    lista.append(7)
    print("Lista iniziale:")
    lista.stampa()
    
    print("Lista ordinata?", lista.is_ordinata())
    
    print("Elemento all'indice 2:", lista.get(2))
    
    print("Rimuovo elemento 5")
    lista.remove(5)
    lista.stampa()
    
    print("Inverto la lista")
    lista.inverti()
    lista.stampa()
    
    print("Accesso a indice non valido:")
    print(lista.get(10))  # Questo solleverà eccezione
except DataStructureIntegrityError as e:
    print("Errore di integrità struttura dati:", e)
