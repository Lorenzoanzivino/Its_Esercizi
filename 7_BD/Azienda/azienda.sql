
CREATE DOMAIN Stringa AS varchar;
CREATE DOMAIN Denaro AS float 
    CHECK (value >= 0);
CREATE DOMAIN Data AS date;

CREATE TABLE dipartimento (
    id integer primary key,
    nome Stringa not null,
    telefono Stringa not null
);

CREATE TABLE impiegato (
    id integer primary key,
    nome Stringa not null,
    cognome Stringa not null,
    data_nascita Data not null,
    stipendio Denaro not null,
    dipartimento integer not null,
    afferisce integer not null,
    dirige integer not null,
    foreign key (afferisce) references dipartimento(id),
    foreign key (dirige) references dipartimento(id)
);

CREATE TABLE progetto (
    id integer primary key,
    nome Stringa not null,
    budget Denaro not null,
    impiegato integer not null,
    partecipa integer not null,

    foreign key (partecipa) references impiegato(id)
);