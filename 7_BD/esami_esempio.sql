create database esami;
\c esami

create domain posint as integer
    check (value > 0);

create domain posint_not_null as posint
    check (value is not null);

create domain string_not_null as varchar
    check (value is not null);

create type indirizzo as (
    via string_not_null,
    cap char(5),
    civico posint_not_null
);

create table docente(
    mat integer primary key, -- implica not null
    cognome varchar(100) not null,
    nome varchar(100) not null,
    email varchar(100) not null
    indirizzo indirizzo not null
);

create table corso(
    codice integer primary key,
    nome varchar not null,
    aula varchar(100) not null
    crediti posint not null
);

create table incarico(
    docente integer not null,
    corso integer not null,
    primary key(docente, corso), -- va messo sotto quando ci sono più elementi con primary key
    foreign key (docente)
        references docente(mat),
    foreign key (corso)
        references corso(codice)
);

-- its@its-Virtual-Machine:~$ docker exec -it its_postgresql psql -U postgres

-- postgres=# create database esami;
-- ERROR:  database "esami" already exists
-- postgres=# \c esami
-- copia e incolla dei codici sql
-- \dt mostra la tabella


-- Modifica e cancellazione di tabelle, schemi e database
-- Modifica
-- ▶ alter table
-- ▶ alter table add column
-- ▶ alter table drop column
-- ▶ alter table alter column
-- ▶ alter table add constraint
-- ▶ alter table drop constraint
-- ▶ etc.
-- Cancellazione
-- ▶ drop table <nome tabella>
-- ▶ drop schema <nome schema>
-- ▶ drop database <nome database>
-- Per i dettagli si veda la documentazione di SQL e quella del DBMS in
-- uso.