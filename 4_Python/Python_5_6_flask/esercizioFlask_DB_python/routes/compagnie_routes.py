from flask import Blueprint, jsonify, request
from datiVoliAerei import DB

compagnie_bp = Blueprint('compagnie_bp', __name__)

@compagnie_bp.route('/CompagniaAerea', methods=['GET', 'POST'])
def gestisci_compagniaAerea():
    compagniaAerea = DB['CompagniaAerea'] 
    
    if request.method == 'GET':
        return jsonify(compagniaAerea)
    
    if request.method == 'POST':
        dati = request.get_json()

        campi_richiesti = ['fondazione', 'nome', 'citta']

        if not dati:
            return jsonify({'errore': 'JSON mancante'}), 400
        
        for campo in campi_richiesti:
            if campo not in dati:
                return jsonify({'errore': f'Il campo "{campo}" è richiesto'}), 400
                
        if dati['citta'] not in DB['Citta']:
            return jsonify({'errore': 'ID Citta non valido'}), 400

        nuovo_id = (len(compagniaAerea) + 1)
        
        nuova_compagniaaerea = {
            'id': nuovo_id,
            'fondazione': dati['fondazione'],
            'nome': dati['nome'],
            'citta': dati['citta']
        }

        compagniaAerea[nuovo_id] = nuova_compagniaaerea
        
        return jsonify(nuova_compagniaaerea), 201