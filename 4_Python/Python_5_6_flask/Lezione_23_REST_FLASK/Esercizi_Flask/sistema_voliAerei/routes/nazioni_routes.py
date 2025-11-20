# Import delle librerie necessarie da Flask
from flask import Blueprint, jsonify, request 

# Import del dizionario DB dal file locale
from datiVoliAerei import DB 

# Creazione del Blueprint
# Un Blueprint è un gruppo di rotte (vie) che possono essere registrate su un'app Flask
nazioni_bp = Blueprint('nazioni_bp', __name__) # -> Definisce un nuovo Blueprint chiamato 'nazioni_bp'

# Rotta per l'intera collezione di Nazioni
@nazioni_bp.route('/Nazioni', methods=['GET', 'POST']) # -> Definisce l'URL /Nazioni per i metodi GET e POST
def gestisci_nazioni(): # -> Funzione che gestisce le richieste a /Nazioni
    
    # Accesso ai dati
    nazioni: dict[int, dict[str, str | int]] = DB['Nazione'] # -> Ottiene il dizionario delle nazioni dal DB
    
    # Logica per il metodo GET
    if request.method == 'GET': # -> Controlla se la richiesta è un GET
        return jsonify(nazioni) # -> Restituisce l'intero dizionario di nazioni in formato JSON
    
    # Logica per il metodo POST
    if request.method == 'POST': # -> Controlla se la richiesta è un POST
        
        # Estrazione dei dati
        dati = request.get_json() # -> Estrae il corpo della richiesta (JSON) inviato dal client
        
        # Validazione dei dati
        if not dati or 'nome' not in dati: # -> Controlla se il JSON esiste e se contiene la chiave 'nome'
            return jsonify({'errore': 'Il campo "nome" è richiesto'}), 400 # -> Restituisce un errore 400 (Bad Request)
        
        # Creazione ID (Metodo non sicuro se si cancella)
        nuovo_id = (len(nazioni) + 1) # -> Calcola un nuovo ID basandosi sulla lunghezza attuale del dizionario
        
        # Creazione del nuovo oggetto
        nuova_nazione = { # -> Costruisce il dizionario per la nuova nazione
            'id': nuovo_id,
            'nome': dati['nome']
        }
        
        # Aggiunta al DB
        nazioni[nuovo_id] = nuova_nazione # -> Aggiunge la nuova nazione al dizionario in memoria usando il nuovo ID come chiave
        
        # Restituisce la risorsa creata
        return jsonify(nuova_nazione), 201 # -> Restituisce la nazione appena creata e lo stato 201 (Created)
    
# Rotta per una Nazione specifica tramite ID
@nazioni_bp.route('/Nazioni/<int:id>', methods=['GET']) # -> Definisce l'URL /Nazioni/<id> per il metodo GET
def gestisci_nazione_singola(id: int): # -> Funzione che gestisce le richieste per un ID specifico
    
    # Accesso ai dati
    nazioni: dict[int, dict[str, str | int]] = DB['Nazione'] # -> Ottiene il dizionario delle nazioni dal DB
    
    # Controllo esistenza ID
    if id in nazioni: # -> Controlla se l'ID fornito nell'URL esiste come chiave nel dizionario
        
        # Risposta in caso di successo
        return jsonify(nazioni[id]) # -> Restituisce i dati della nazione specifica trovata
    else:
        
        # Risposta in caso di errore
        return jsonify({'errore': 'Nazione non trovata'}), 404 # -> Restituisce un errore 404 (Not Found)