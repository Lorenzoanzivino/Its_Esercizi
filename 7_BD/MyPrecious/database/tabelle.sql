CREATE DOMAIN stringa as varchar (255);
CREATE DOMAIN IntGEZ as integer
    check (value >= 0);
CREATE DOMAIN RealGEZ as real
    check (value >= 0);
CREATE DOMAIN Prezzo as real
    check (value >= 0);

CREATE TYPE TipoCategoria as ENUM
    ('Dipinto', 'Scultura', 'Mosaico', 'Manoscritto');


CREATE TABLE nazione (
    nome stringa PRIMARY KEY
);

CREATE TABLE regione (
    nome stringa NOT NULL,
    nazione stringa NOT NULL,
    PRIMARY KEY (nome, nazione),
    FOREIGN KEY (nazione) REFERENCES nazione(nome)
);

CREATE TABLE citta (
    nome stringa NOT NULL,
    regione stringa NOT NULL,
    nazione stringa NOT NULL,
    PRIMARY KEY (nome, regione, nazione),
    FOREIGN KEY (regione, nazione) REFERENCES regione(nome, nazione)
);

CREATE TABLE autore(
    nome_arte stringa PRIMARY KEY,
    data_nascita date NOT NULL,
    data_morte date,
    citta stringa NOT NULL,
    regione stringa NOT NULL,
    nazione stringa NOT NULL,
    FOREIGN KEY (citta, regione, nazione) REFERENCES citta(nome, regione, nazione)
);

CREATE TABLE categoria (
    id integer PRIMARY KEY,
    tipo tipoCategoria NOT NULL
);

CREATE TABLE esposizionePermanente(
    nome stringa PRIMARY KEY,
    tema stringa NOT NULL,
    data_inizio date NOT NULL
);

CREATE TABLE esposizioneTemporanea (
    nome stringa PRIMARY KEY,
    tema stringa NOT NULL,
    prez_acc Prezzo NOT NULL,
    data_inizio date NOT NULL,
    data_fine date NOT NULL
);

CREATE TABLE opera (
    nome stringa PRIMARY KEY,
    anno_realizzazione IntGEZ NOT NULL,
    tecnica stringa NOT NULL,
    corrente_artistica stringa NOT NULL,
    categoria integer NOT NULL,
    autore stringa NOT NULL,
    esposizionePermanente stringa,
    esposizioneTemporanea stringa,
    FOREIGN KEY (categoria) REFERENCES categoria(id),
    FOREIGN KEY (autore) REFERENCES autore(nome_arte),
    FOREIGN KEY (esposizionePermanente) REFERENCES esposizionePermanente(nome),
    FOREIGN KEY (esposizioneTemporanea) REFERENCES esposizioneTemporanea(nome),
    CHECK (
        (esposizionePermanente IS NOT NULL AND esposizioneTemporanea IS NULL)
        OR (esposizionePermanente IS NULL AND esposizioneTemporanea IS NOT NULL)
        OR (esposizionePermanente IS NULL AND esposizioneTemporanea IS NULL)
    )
);

CREATE TABLE visitatore(
    id integer PRIMARY KEY
);

CREATE TABLE tariffa(
    nome stringa PRIMARY KEY,
    prez_base prezzo NOT NULL
);

CREATE TABLE biglietto_standard(
    id integer PRIMARY KEY,
    visitatore integer UNIQUE NOT NULL,
    tariffa stringa NOT NULL,
    esposizionePermanente stringa NOT NULL,
    FOREIGN KEY (visitatore) REFERENCES visitatore(id),
    FOREIGN KEY (tariffa) REFERENCES tariffa(nome),
    FOREIGN KEY (esposizionePermanente) REFERENCES esposizionePermanente(nome)
);

CREATE TABLE biglietto_ext_acc(
    id integer PRIMARY KEY,
    visitatore integer UNIQUE NOT NULL,
    tariffa stringa NOT NULL,
    esposizionePermanente stringa NOT NULL,
    esposizioneTemporanea stringa NOT NULL,
    FOREIGN KEY (visitatore) REFERENCES visitatore(id),
    FOREIGN KEY (tariffa) REFERENCES tariffa(nome),
    FOREIGN KEY (esposizionePermanente) REFERENCES esposizionePermanente(nome),
    FOREIGN KEY (esposizioneTemporanea) REFERENCES esposizioneTemporanea(nome)
);