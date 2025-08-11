-- TABELLE
CREATE TABLE Persona (
    codicefiscale codicefiscale PRIMARY KEY,
    Nome stringa NOT NULL,
    Indirizzo stringa NOT NULL,
    NumeroTelefono telefono NOT NULL
);

CREATE TABLE Officina (
    id_officina integer PRIMARY KEY,
    Nome stringa NOT NULL,
    Indirizzo stringa NOT NULL
);

CREATE TABLE Staff (
    id_staff integer PRIMARY KEY,
    codicefiscale_staff codicefiscale UNIQUE NOT NULL,
    FOREIGN KEY (codicefiscale_staff) REFERENCES Persona(codicefiscale)
);

CREATE TABLE Proprietario (
    id_proprietario integer PRIMARY KEY,
    codicefiscale_proprietario codicefiscale UNIQUE NOT NULL,
    FOREIGN KEY (codicefiscale_proprietario) REFERENCES Persona(codicefiscale)
);

CREATE TABLE Dipendente (
    id_dipendente integer PRIMARY KEY,
    anni_servizio integer NOT NULL,
    FOREIGN KEY (id_dipendente) REFERENCES Staff(id_staff)
);

CREATE TABLE Direttore (
    id_direttore integer PRIMARY KEY,
    DataNascita data_nascita NOT NULL,
    FOREIGN KEY (id_direttore) REFERENCES Staff(id_staff)
);

CREATE TABLE Veicolo (
    targa VARCHAR(10) PRIMARY KEY,
    Modello stringa NOT NULL,
    Tipo stringa NOT NULL,
    chilometri integer NOT NULL
);

CREATE TABLE Riparazione (
    id_riparazione integer PRIMARY KEY,
    Codice stringa NOT NULL,
    DataAccettazione data_nascita NOT NULL,
    OraAccettazione orario NOT NULL,
    targa_veicolo VARCHAR(10) NOT NULL,
    id_proprietario integer NOT NULL,
    FOREIGN KEY (targa_veicolo) REFERENCES Veicolo(targa),
    FOREIGN KEY (id_proprietario) REFERENCES Proprietario(id_proprietario)
);

CREATE TABLE RiparazioneTerminata (
    id_riparazione integer PRIMARY KEY,
    DataConsegna data_nascita NOT NULL,
    OraConsegna orario NOT NULL,
    targa_veicolo VARCHAR(10) NOT NULL,
    FOREIGN KEY (id_riparazione) REFERENCES Riparazione(id_riparazione),
    FOREIGN KEY (targa_veicolo) REFERENCES Veicolo(targa)
);

CREATE TABLE LavoraPresso (
    id_dipendente integer NOT NULL,
    id_officina integer NOT NULL,
    inizio_servizio data_nascita NOT NULL,
    fine_servizio data_nascita,
    PRIMARY KEY (id_dipendente, id_officina),
    FOREIGN KEY (id_dipendente) REFERENCES Dipendente(id_dipendente),
    FOREIGN KEY (id_officina) REFERENCES Officina(id_officina)
);

