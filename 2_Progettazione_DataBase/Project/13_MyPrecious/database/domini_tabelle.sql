CREATE DOMAIN stringa as varchar (255);
CREATE DOMAIN IntGEZ as integer
    check (value >= 0);
CREATE DOMAIN RealGEZ as real
    check (value >= 0);
CREATE DOMAIN prezzo as real
    check (value >= 0);


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
    check (data_morte > data_nascita),
    citta stringa NOT NULL,
    regione stringa NOT NULL,
    nazione stringa NOT NULL,
    FOREIGN KEY (citta, regione, nazione) REFERENCES citta(nome, regione, nazione)
);

CREATE TABLE categoria (
    nome stringa PRIMARY KEY
);

CREATE TABLE opera (
    nome stringa PRIMARY KEY,
    anno_realizzazione IntGEZ NOT NULL,
    tecnica stringa NOT NULL,
    corrente_artistica stringa NOT NULL,
    categoria stringa NOT NULL,
    autore stringa NOT NULL,
    FOREIGN KEY (categoria) REFERENCES categoria(nome),
    FOREIGN KEY (autore) REFERENCES autore(nome_arte)
);

CREATE TABLE esposizione (
    data_inizio date NOT NULL,
    tema stringa NOT NULL,
    nome stringa PRIMARY KEY
);

CREATE TABLE op_esp (
    opera stringa NOT NULL,
    esposizione stringa NOT NULL,
    PRIMARY KEY (opera, esposizione),
    FOREIGN KEY (opera) REFERENCES opera(nome),
    FOREIGN KEY (esposizione) REFERENCES esposizione(nome)
);

CREATE TABLE esposizionePermanente (
    esposizione_nome stringa PRIMARY KEY,
    FOREIGN KEY (esposizione_nome) REFERENCES esposizione(nome)
);

CREATE TABLE esposizioneTemporanea (
    prez_acc prezzo NOT NULL,
    data_fine date NOT NULL,
    esposizione_nome stringa PRIMARY KEY,
    FOREIGN KEY (esposizione_nome) REFERENCES esposizione(nome)
);

CREATE TABLE tariffa (
    nome stringa PRIMARY KEY,
    prez_base prezzo NOT NULL
);

CREATE TABLE biglietto (
    id integer PRIMARY KEY,
    tariffa stringa NOT NULL,
    FOREIGN KEY (tariffa) REFERENCES tariffa(nome)
);

CREATE TABLE biglietto_standard (
    biglietto_id integer PRIMARY KEY,
    FOREIGN KEY (biglietto_id) REFERENCES biglietto(id)
);

CREATE TABLE biglietto_ext_acc (
    biglietto_id integer PRIMARY KEY,
    data_validita date NOT NULL,
    FOREIGN KEY (biglietto_id) REFERENCES biglietto(id)
);

CREATE TABLE esp_temp_bigE (
    biglietto_ext_acc integer NOT NULL,
    esposizioneTemporanea stringa NOT NULL,
    PRIMARY KEY (biglietto_ext_acc, esposizioneTemporanea),
    FOREIGN KEY (biglietto_ext_acc) REFERENCES biglietto_ext_acc(biglietto_id),
    FOREIGN KEY (esposizioneTemporanea) REFERENCES esposizioneTemporanea(esposizione_nome)
);

-- Vincolo: due opere dello stesso autore non possono avere lo stesso nome
ALTER TABLE opera
ADD CONSTRAINT unicita_nome_autore UNIQUE (nome, autore);

-- Vincolo: la data di validità del biglietto >= data di vendita
-- Nota: se hai una colonna "data_vendita" nella tabella biglietto, sostituisci CURRENT_DATE
ALTER TABLE biglietto_ext_acc
ADD CONSTRAINT ck_data_validita CHECK (data_validita >= data_vendita);