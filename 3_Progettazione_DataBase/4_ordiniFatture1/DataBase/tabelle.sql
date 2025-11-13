-- DOMINI
CREATE DOMAIN stringa AS varchar;
CREATE DOMAIN reale AS real CHECK (VALUE >= 0);
CREATE DOMAIN realeI01 AS real CHECK (VALUE > 0 AND VALUE < 1);
CREATE DOMAIN intero AS integer CHECK (VALUE >= 0);
CREATE DOMAIN codicefiscale AS char(16) CHECK (VALUE ~ '^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$');
CREATE DOMAIN telefono AS varchar(20) CHECK (VALUE ~ '^\+?[0-9]{1,3}[\s\-]?[0-9]{6,14}$');
CREATE DOMAIN partitaiva AS char(11) CHECK (VALUE ~ '^[A-Z]{2}?[0-9A-Z]{8,13}$');
CREATE DOMAIN email AS varchar CHECK (VALUE ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$');
CREATE DOMAIN data_nascita AS date;

-- TIPI ENUM E COMPOSITI
CREATE TYPE stato AS ENUM ('in_preparazione', 'inviato', 'da_saldare', 'saldato');
CREATE TYPE indirizzo AS (via stringa, civico stringa, cap char(5));

-- TABELLE
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

CREATE TABLE direttore (
    nome stringa NOT NULL,
    cognome stringa NOT NULL,
    cf codicefiscale PRIMARY KEY,
    data_nascita data_nascita NOT NULL,
    anni_servizio intero NOT NULL,
    citta stringa NOT NULL,
    regione stringa NOT NULL,
    nazione stringa NOT NULL,
    FOREIGN KEY (citta, regione, nazione) REFERENCES citta(nome, regione, nazione)
);

CREATE TABLE dipartimento (
    nome stringa PRIMARY KEY,
    indirizzo indirizzo NOT NULL,
    direttore codicefiscale,
    FOREIGN KEY (direttore) REFERENCES direttore(cf)
);

CREATE TABLE fornitore (
    ragione_sociale stringa NOT NULL,
    partitaiva partitaiva PRIMARY KEY,
    indirizzo indirizzo NOT NULL,
    telefono telefono NOT NULL,
    email email NOT NULL
);

CREATE TABLE ordine (
    id integer PRIMARY KEY,
    data_stipula date NOT NULL,
    imponibile reale NOT NULL,
    aliquotaiva realeI01 NOT NULL,
    descrizione stringa NOT NULL,
    stato stato NOT NULL,
    fornitore partitaiva NOT NULL,
    dipartimento stringa NOT NULL,
    FOREIGN KEY (fornitore) REFERENCES fornitore(partitaiva),
    FOREIGN KEY (dipartimento) REFERENCES dipartimento(nome)
);