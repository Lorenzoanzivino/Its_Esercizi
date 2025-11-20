from flask import Flask

# Importa tutti i tuoi Blueprint
from routes.nazioni_routes import nazioni_bp
from routes.citta_routes import citta_bp
from routes.aereoporti_routes import aereoporti_bp
from routes.compagnie_routes import compagnie_bp
from routes.voli_routes import voli_bp

# 1. Crea l'app
app = Flask(__name__)

# 2. Registra i Blueprint sull'app
app.register_blueprint(nazioni_bp)
app.register_blueprint(citta_bp)
app.register_blueprint(aereoporti_bp)
app.register_blueprint(compagnie_bp)
app.register_blueprint(voli_bp)

# 3. Esegui il server (solo da questo file)
if __name__ == '__main__':
    app.run(debug=True)