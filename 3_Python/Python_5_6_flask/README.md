## 🏗️ Struttura cartelle di un progetto completo

```bash
CartellaProgetto/
├── 📂 docs/                        <-- (La "Memoria": Analisi, Design, etc.)
│   ├── Analisi/
│   ├── Design/
│   │   ├── Python/
│   │   ├── Postgress/
│   │   └── RestAPI/
│   └── DataBase/
│
├── 🚀 app/                         <-- (Il "Codice Attivo")
│   ├── __init__.py                 <-- Qui inizializzi l'app Flask
│   │
│   ├── models/                     <-- (EX data_model del Prof)
│   │   ├── __init__.py             <-- Rende la cartella un package
│   │   ├── citta.py                <-- File del prof
│   │   └── nazione.py              <-- File del prof
│   │
│   ├── data/                       <-- (EX dp del Prof - Data Persistence)
│   │   ├── __init__.py
│   │   ├── mockup_db.json          <-- Il "database" JSON del prof
│   │   ├── mockup_db_init.json
│   │   └── data_manager.py         <-- (Ex utils.py) Funzioni per leggere il JSON
│   │
│   ├── routes.py                   <-- Qui importi le classi da models/ e i dati da data/
│   │
│   ├── static/                     <-- CSS, IMG (Invariato)
│   └── templates/                  <-- HTML (Invariato)
│
├── 🧪 tests/                       <-- NUOVA CARTELLA TEST
│   ├── __init__.py
│   ├── test_models.py              <-- (Ex classi_test.py)
│   └── test_routes.py              <-- (Ex test.py)
│
├── 🐍 venv/                        <-- (Invariato)
├── ▶️ run.py                       <-- (Ex main.py del prof)
├── 📄 requirements.txt
└── 📖 README.md
```

### La Nuova Struttura Consigliata

Immagina di dividere la cartella principale VoliAerei in due macro-aree: docs (il tuo vecchio materiale) e app (il nuovo codice Flask).

Come migrare i tuoi file attuali

Ecco come dovresti spostare i file che hai citato nella nuova struttura:

- 1. La Cartella docs/ (La memoria del progetto)

Sposta qui tutto ciò che non serve al computer per eseguire il programma, ma serve a te per capire come è fatto.

    Cosa spostare qui: I file .vpp (Visual Paradigm), i PDF, i diagrammi immagini, e i file .txt di appunti.

    Sottocartelle: Mantieni pure la tua divisione analisi, design (per i diagrammi di flusso) e dataBase (per i diagrammi ER).

- 2. La Cartella app/ (Il codice attivo)

Qui va solo il codice che Flask deve eseguire.

    - Il tuo file.py (parte di design python):

        Probabilmente contiene classi o funzioni logiche. Questo codice va integrato in routes.py (se gestisce le risposte web) o in un nuovo file services.py (se fa calcoli complessi sui voli).

    - Il tuo file.sql (parte creazione database):

        In Flask, solitamente si usa un ORM chiamato SQLAlchemy. Invece di scrivere SQL puro, scriverai classi Python dentro models.py.

        Nota: Se vuoi mantenere l'SQL puro, metti il file .sql in una cartella db_scripts/ alla radice, ma non dentro app/.

### Perché questa struttura è migliore?

    Standard di Settore: Chiunque conosca Flask, aprendo la cartella, saprà esattamente dove trovare i file HTML (templates), dove trovare la logica (routes) e dove trovare i CSS (static).

    Pulizia: Quando dovrai distribuire il sito (deploy), caricherai solo la cartella app e run.py, lasciando a casa gigabyte di PDF e diagrammi che non servono al server.

    Cicolarità: Evita errori di importazione (circular imports) che sono comuni in Python se i file sono sparsi senza logica.

### I file essenziali alla "Radice"

Al livello più alto (dentro VoliAerei/) dovresti avere solo i file di gestione:

    run.py: È un file piccolissimo che serve solo ad avviare tutto. Esempio:

    from app import create_app

    app = create_app()

    if __name__ == '__main__':
        app.run(debug=True)

    - requirements.txt: Fondamentale se lavori in team o cambi PC. Lo generi con pip freeze > requirements.txt.

    - .gitignore: Per dire a Git di ignorare la cartella venv/ e i file compilati .pyc.