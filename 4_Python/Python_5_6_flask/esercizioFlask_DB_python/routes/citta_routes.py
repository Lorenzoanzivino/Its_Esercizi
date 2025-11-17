from flask import Blueprint, jsonify, request
from datiVoliAerei import DB

citta_bp = Blueprint('citta_bp', __name__)

@citta_bp.route('/Citta', methods=['GET', 'POST'])
def gestisci_citta():
    citta = DB['Citta'] 
    
    if request.method == 'GET':
        return jsonify(citta)
    
    if request.method == 'POST':
        dati = request.get_json()
        campi_richiesti = ['nome', 'n_abitanti', 'nazione']

        if not dati:
            return jsonify({'errore': 'JSON mancante'}), 400
        for campo in campi_richiesti:
            if campo not in dati:
                return jsonify({'errore' : f'Il campo "{campo}" è richiesto'}), 400
        
        if dati['nazione'] not in DB['Nazione']:
            return jsonify({'errore': 'ID Nazione non valido'}), 400
        
        nuovo_id = (len(citta) + 1)
        nuova_citta = {
            'id': nuovo_id,
            'nome': dati['nome'],
            'n_abitanti': dati['n_abitanti'],
            'nazione': dati['nazione']
        }
        citta[nuovo_id] = nuova_citta
        return jsonify(nuova_citta), 201