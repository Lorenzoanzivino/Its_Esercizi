# 🗄 Progetto Database

Questa directory raccoglie tutti i materiali relativi alla **progettazione e implementazione di un database** per il progetto software.  
Segue la stessa logica del README di progettazione: dalla struttura concettuale al modello implementabile e all’utilizzo pratico tramite strumenti di gestione.

---

## 📁 Struttura della cartella

### 🔹 `Database` — Dalla progettazione all’implementazione
In questa fase si traduce il modello concettuale in un **database relazionale completo**, pronto per essere popolato e interrogato.

**Contenuti principali:**
- **Avvio Docker PostgreSQL:**  
  Istruzioni e configurazioni per avviare un’istanza PostgreSQL tramite Docker, in modo rapido e isolato.  
  Include configurazioni di porta, volume persistente e credenziali.
- **Diagramma ristrutturato SQL:**  
  Adattamento del modello concettuale (UML) alle specifiche SQL, evidenziando relazioni tra tabelle, chiavi primarie, chiavi esterne e vincoli.
- **Creazione domini:**  
  Definizione di tipi di dato personalizzati (domain) per garantire consistenza e validità dei dati.
- **Creazione tabelle:**  
  Definizione di tutte le tabelle necessarie, con colonne, tipi di dati, chiavi primarie e vincoli di integrità.
- **Alter Table:**  
  Modifiche successive alle tabelle per aggiungere vincoli, colonne o modificare strutture già esistenti.
- **Trigger:**  
  Definizione di trigger per automatizzare controlli, aggiornamenti o log di modifiche sui dati.
- **Foreign Key:**  
  Definizione di relazioni tra tabelle per garantire l’integrità referenziale del database.
- **Inserimento dati:**  
  Script SQL per popolare le tabelle con dati di esempio o reali.
- **Utilizzo di pgAdmin:**  
  Guida base all’uso di pgAdmin per la gestione visuale del database, esecuzione query, controllo schemi e monitoraggio.
- **Query SQL:**  
  Esempi di query per interrogare il database, ottenere report, join tra tabelle e manipolazione dei dati.

**Obiettivo:**  
Tradurre il progetto concettuale in un **database relazionale funzionante**, pronto per essere interrogato e integrato con applicazioni front-end o back-end.

---

## 🧠 Competenze acquisite

- Configurazione e avvio di **PostgreSQL** con Docker
- Modellazione e ristrutturazione di **diagrammi concettuali in SQL**
- Definizione di **domini, tabelle, vincoli e trigger**
- Gestione di **chiavi primarie e chiavi esterne**
- Popolamento dei dati e test del database
- Interrogazione con **query SQL complesse**
- Utilizzo di strumenti di gestione visuale (**pgAdmin**) per amministrazione e debugging

---

## ⚙️ Strumenti e requisiti

- [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/)
- [PostgreSQL](https://www.postgresql.org/)
- [pgAdmin](https://www.pgadmin.org/)
- Editor consigliato: **Visual Studio Code**, **DBeaver**, **DataGrip** o simili
- Conoscenze base di SQL relazionale

---

## 🐳 Avvio Docker e PostgreSQL

Assicurati di avere Docker installato.  
Per creare e avviare un container PostgreSQL:

```bash
docker run --name its_postgresql -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
```

Spiegazione comandi:

- --name its_postgresql → nome del container.
- -e POSTGRES_PASSWORD=postgres → password dell’utente postgres.
- -p 5432:5432 → mappatura porta host → container.
- -d postgres → esegue il container in background.

Per entrare nel container e usare psql:
```bash
docker exec -it its_postgresql psql -U postgres
```
- exec -it → entra interattivamente nel container.
- psql -U postgres → avvia l’interfaccia a riga di comando di PostgreSQL come utente postgres.

---

## 📂 Creazione Database e Connessione

All’interno di psql:
```bash
-- Creazione del database
CREATE DATABASE its_database;

-- Connessione al database appena creato
\c its_database
```
- CREATE DATABASE <nome> → crea un nuovo database.
- \c <nome_database> → connette il terminale SQL al database specificato.

--- 

## 🏗 Creazione Domini

```bash
CREATE DOMAIN stringa AS VARCHAR(255);
CREATE DOMAIN int_positivo AS INTEGER CHECK (VALUE >= 0);
CREATE DOMAIN real_positivo AS REAL CHECK (VALUE >= 0);
```
I domini sono tipi personalizzati con vincoli già inclusi (es: lunghezza, valori positivi).

--- 

## 📑 Creazione Tabelle

```bash
CREATE TABLE autore (
    id SERIAL PRIMARY KEY,
    nome stringa NOT NULL,
    cognome stringa NOT NULL,
    data_nascita DATE NOT NULL,
    data_morte DATE
);

CREATE TABLE libro (
    id SERIAL PRIMARY KEY,
    titolo stringa NOT NULL,
    anno_pubblicazione int_positivo,
    autore_id INTEGER,
    FOREIGN KEY (autore_id) REFERENCES autore(id)
);
```
---

## 🔧 Alter Table e Vincoli

```bash
-- Aggiunta vincolo foreign key
ALTER TABLE libro
ADD CONSTRAINT fk_autore FOREIGN KEY (autore_id)
REFERENCES autore(id);
```
---

## ⚡ Trigger

```bash
CREATE OR REPLACE FUNCTION check_date_morte()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.data_morte IS NOT NULL AND NEW.data_morte <= NEW.data_nascita THEN
        RAISE EXCEPTION 'La data di morte deve essere successiva alla nascita';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_autore_date
BEFORE INSERT OR UPDATE ON autore
FOR EACH ROW
EXECUTE FUNCTION check_date_morte();
```
Il trigger verifica che la data di morte sia coerente con la data di nascita.

---

## 💾 Inserimento Dati

```bash
INSERT INTO autore (nome, cognome, data_nascita)
VALUES ('Lorenzo', 'Anzivino', '2000-01-01');

INSERT INTO libro (titolo, anno_pubblicazione, autore_id)
VALUES ('Progetto DB', 2025, 1);
```

---

## 🖥 Utilizzo di pgAdmin

Apri PGAdmin e crea una nuova connessione al server PostgreSQL.

Host: localhost, porta: 5432, utente: postgres, password: postgres.

Visualizza tabelle, esegui query e monitora il database.

---

## 📊 Query di esempio

```bash
-- Seleziona tutti gli autori
SELECT * FROM autore;

-- Filtra autori nati dopo il 1990
SELECT * FROM autore WHERE data_nascita > '1990-01-01';

-- Conteggio libri
SELECT COUNT(*) FROM libro;

-- Join tra autore e libro
SELECT a.nome, a.cognome, l.titolo
FROM autore a
JOIN libro l ON a.id = l.autore_id;
```

---

## 👨‍💻 Autore
**Lorenzo Anzivino**  
Studente ITS – Corso Application Cloud Developer  
Appassionato di database relazionali, progettazione dati e ottimizzazione di query SQL.

---

## 🧩 Note finali
La cartella contiene **script SQL completi**, diagrammi, istruzioni per l’avvio di PostgreSQL e esempi pratici di utilizzo.  
Tutti i materiali sono pensati per essere una guida completa alla gestione di un database relazionale efficiente e coerente con il modello progettuale.

---

## 🐳 Spiegazione Comandi Docker

**Spiegazione comandi:**

- `--name its_postgresql` → nome del container.
- `-e POSTGRES_PASSWORD=postgres` → password dell’utente postgres.
- `-p 5432:5432` → mappatura porta host → container.
- `-d postgres` → esegue il container in background.

Per entrare nel container e usare psql:

```Bash
docker exec -it its_postgresql psql -U postgres
```
- exec -it → entra interattivamente nel container.

- psql -U postgres → avvia l’interfaccia a riga di comando di PostgreSQL come utente postgres.