begin transaction;

CREATE DOMAIN PosInteger AS Integer
    check (value >= 0);

CREATE DOMAIN StringaM AS VARCHAR(100);

CREATE DOMAIN CodIATA AS CHAR(3);

create table Compagnia(
    nome StringaM primary key,
    annoFondaz PosInteger
);

create table Volo(
    codice PosInteger,
    comp StringaM,
    durataMinuti PosInteger not null,
    primary key (codice, comp),

    foreign key (comp) references Compagnia(nome)
);

create table Aeroporto(
    codice CodIATA primary key, 
    nome StringaM not null
);

create table LuogoAeroporto(
    aeroporto CodIATA primary key, 
    citta StringaM not null, 
    nazione StringaM not null, 
    foreign key (aeroporto) 
        references Aeroporto(codice) deferrable
);

create table ArrPart(
    codice PosInteger, 
    comp StringaM , 
    arrivo CodIATA not null,
    partenza CodIATA not null,
    primary key (codice, comp),

    foreign key (codice, comp) references Volo(codice, comp) deferrable,
    foreign key (arrivo) references Aeroporto(codice),
    foreign key (partenza) references Aeroporto(codice)
);

alter table volo add foreign key (codice, comp) references ArrPart(codice, comp) deferrable;

alter table aeroporto add foreign key (codice) references LuogoAeroporto(aeroporto) deferrable;

commit;