from flask import Blueprint, jsonify, request
from datiVoliAerei import DB

aereoporti_bp = Blueprint('aereoporti_bp', __name__)

@aereoporti_bp.route('/Aereoporti', methods=['GET', 'POST'])
def gestisci_aereoporti():
    aereoporti = DB['Aereoporto'] 
    
    if request.method == 'GET':
        return jsonify(aereoporti)
    
    if request.method == 'POST':
        dati = request.get_json()
        campi_richiesti = ['nome', 'codice', 'citta']

        if not dati:
            return jsonify({'errore': 'JSON mancante'}), 400
        
        for campo in campi_richiesti:
            if campo not in dati:
                return jsonify({'errore' : f'Il campo "{campo}" è richiesto'}), 400
            
        if dati['citta'] not in DB['Citta']:
            return jsonify ({'errore': 'ID Citta non valido'}), 400
        
        nuovo_id  = (len(aereoporti) + 1)
        nuova_aereoporto = {
            'id': nuovo_id,
            'nome': dati['nome'],
            'codice': dati['codice'],
            'citta': dati['citta']
        }

        aereoporti[nuovo_id] = nuova_aereoporto
        
        return jsonify(nuova_aereoporto), 201