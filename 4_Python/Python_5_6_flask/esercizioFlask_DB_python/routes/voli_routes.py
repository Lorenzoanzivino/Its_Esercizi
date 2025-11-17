from flask import Blueprint, jsonify, request
from datiVoliAerei import DB

voli_bp = Blueprint('voli_bp', __name__)

@voli_bp.route('/Voli', methods=['GET', 'POST'])
def gestisci_voli():
    voli = DB['Volo'] 
    
    if request.method == 'GET':
        return jsonify(voli)
    
    if request.method == 'POST':
        dati = request.get_json()

        campi_richiesti = ['durata_in_minuti', 'codice', 'compagniaAerea', 'aeroporto_partenza', 'aeroporto_arrivo']
        
        if not dati:
            return jsonify({'errore': 'JSON mancante'}), 400
        
        for campo in campi_richiesti:
            if campo not in dati:
                return jsonify({'errore': f'Il campo "{campo}" è richiesto'}), 400
        
        if dati['compagniaAerea'] not in DB['CompagniaAerea']:
            return jsonify({'errore': 'ID CompagniaAerea non valido'}), 400
        if dati['aeroporto_partenza'] not in DB['Aereoporto']:
            return jsonify({'errore': 'ID aeroporto_partenza non valido'}), 400
        if dati['aeroporto_arrivo'] not in DB['Aereoporto']:
            return jsonify({'errore': 'ID aeroporto_arrivo non valido'}), 400

        nuovo_id = len(voli) + 1
        
        nuovo_volo = {
            'id': nuovo_id,
            'durata_in_minuti': dati['durata_in_minuti'],
            'codice': dati['codice'],
            'compagniaAerea': dati['compagniaAerea'],
            'aeroporto_partenza': dati['aeroporto_partenza'],
            'aeroporto_arrivo': dati['aeroporto_arrivo']
        }

        voli[nuovo_id] = nuovo_volo
        
        return jsonify(nuovo_volo), 201