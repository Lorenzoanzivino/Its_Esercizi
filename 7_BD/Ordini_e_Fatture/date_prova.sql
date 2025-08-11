-- DATI DI PROVA

INSERT INTO nazione (nome) VALUES 
('Italia'),
('Francia');

INSERT INTO regione (nome, nazione) VALUES
('Lazio', 'Italia'),
('Lombardia', 'Italia'),
('Île-de-France', 'Francia');

INSERT INTO citta (nome, regione, nazione) VALUES
('Roma', 'Lazio', 'Italia'),
('Milano', 'Lombardia', 'Italia'),
('Parigi', 'Île-de-France', 'Francia');

INSERT INTO direttore (nome, cognome, cf, data_nascita, anni_servizio, citta, regione, nazione) VALUES
('Mario', 'Rossi', 'RSSMRA70A01H501U', '1970-01-01', 15, 'Roma', 'Lazio', 'Italia'),
('Luigi', 'Bianchi', 'BNCLGU75B15F205Z', '1975-02-15', 10, 'Milano', 'Lombardia', 'Italia');

INSERT INTO dipartimento (nome, indirizzo, direttore) VALUES
('Logistica', ROW('Via dei Magazzini', '10', '00100'), 'RSSMRA70A01H501U'),
('Acquisti', ROW('Corso Italia', '25', '20100'), 'BNCLGU75B15F205Z');

INSERT INTO fornitore (ragione_sociale, partitaiva, indirizzo, telefono, email) VALUES
('Forniture SRL', 'IT12345678901', ROW('Via Fornitori', '5', '00100'), '+39 061234567', 'info@fornituresrl.it'),
('Materiali Spa', 'IT98765432109', ROW('Viale Materiali', '12', '20100'), '+39 029876543', 'contatti@materialispa.it');

INSERT INTO ordine (id, data_stipula, imponibile, aliquotaiva, descrizione, stato, fornitore, dipartimento) VALUES
(1, '2025-01-15', 1000.00, 0.22, 'Fornitura carta', 'in_preparazione', 'IT12345678901', 'Logistica'),
(2, '2025-02-01', 2500.00, 0.22, 'Acquisto toner', 'inviato', 'IT98765432109', 'Acquisti'),
(3, '2025-02-10', 1500.00, 0.22, 'Materiali imballaggio', 'da_saldare', 'IT12345678901', 'Logistica');
