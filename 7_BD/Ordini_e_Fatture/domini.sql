-- Tipi di dato non standard

CREATE DOMAIN stringa as varchar;
CREATE DOMAIN reale as real
    check (value >= 0);
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