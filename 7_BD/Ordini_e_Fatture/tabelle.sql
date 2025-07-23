-- Tipi di dato non standard

CREATE DOMAIN stringa as varchar;
CREATE DOMAIN reale as real
    check (value >= 0);
CREATE DOMAIN realeI01 as real
    check (value > 0 and value < 1);
CREATE DOMAIN intero as integer
    check (value >= 0);
CREATE DOMAIN CodiceFiscale as char(16)
    check (value ~ '^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$');
CREATE DOMAIN Telefono as varchar(20)
    check (value ~ '^\+?[0-9]{1,3}[\s\-]?[0-9]{6,14}$');
CREATE DOMAIN PartitaIVA as char(11)
    check (value ~ '^[A-Z]{2}?[0-9A-Z]{8,13}$');
CREATE DOMAIN Email as varchar
    check (value ~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$');
CREATE DOMAIN data_nascita as Date;

CREATE TYPE stato as ENUM ( 'in_preparazione',  'inviato',  'da_saldare', 'saldato');
CREATE TYPE Indirizzo as (via stringa, civico stringa, cap char(5));

-- TABELLE

CREATE TABLE Nazione(
    nome StringaM primary key,
);

CREATE TABLE Regione(
    nome StringaM not null,
    nazione StringaM not null,
    primary key (nome, regione),

    foreign key (nazione) references Nazione(nome)
);

CREATE TABLE Citta(
    nome StringaM not null,
    regione StringaM not null,
    nazione StringaM nott, null,
    primary key (nome, regione, nazione),
    
    foreign key (regione, nazione) references Regione(nome, nazione)
);

CREATE TABLE Direttore(
    nome StringaM not null,
    cognome StringaM not null,
    cf CodifceFiscale primary key,
    data_nascita Date not null,
    anni_servizio intero not null,
    Citta StringaM not null,
    regione StringaM not null,
    nazione StringaM not null,

    foreign key (citta, regione, nazione) references Citta(nome, regione, nazione)
);

CREATE TABLE Dipartimento(
    nome StringaM not null,
    Indirizzo Indirizzo primary key,
    direttore StringaM nott null,

    foreign key (direttore) references Direttore(cf)
);

CREATE TABLE Fornitore(
    regione_sociale StringaM not null,
    partitaIVA PartitaIVA primary key,
    indirizzo Indirizzo not null,
    telefono Telefono not null,
    email Email not null
);

CREATE TABLE Ordine(
    data_stipula Date not null,
    imponibile reale not null,
    aliquotaIVA realeI01 not null,
    descrizione StringaM not null,
    stato Stato not null,
    id integer primary key,
    fornitore partitaIVA not null,
    dipartimento StringaM not null,

    foreign key (fornitore) references Fornitore(partitaIVA),
    foreign key (dipartimento) references Dipartimento(nome)
);
