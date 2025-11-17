from flask import Blueprint, jsonify, request

from datiVoliAerei import DB 

# Creiamo il Blueprint
nazioni_bp = Blueprint('nazioni_bp', __name__)

@nazioni_bp.route('/Nazioni', methods=['GET', 'POST'])
def gestisci_nazioni():
    nazioni: dict[int, dict[str, str | int]] = DB['Nazione'] 
    
    if request.method == 'GET':
        return jsonify(nazioni)
    
    if request.method == 'POST':
        dati = request.get_json()
        if not dati or 'nome' not in dati:
            return jsonify({'errore': 'Il campo "nome" è richiesto'}), 400
        
        nuovo_id = (len(nazioni) + 1)
        nuova_nazione = {
            'id': nuovo_id,
            'nome': dati['nome']
        }
        nazioni[nuovo_id] = nuova_nazione
        return jsonify(nuova_nazione), 201