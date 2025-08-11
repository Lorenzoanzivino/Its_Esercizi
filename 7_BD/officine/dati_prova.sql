-- Inserimento dati di prova

-- 1. Persone
INSERT INTO Persona (codicefiscale, Nome, Indirizzo, NumeroTelefono) VALUES
('RSSMRA80A01H501V', 'Mario Rossi', 'Via Roma 10, Milano', '333-1234567'),
('VRDLGI85C05F205C', 'Luigi Verdi', 'Corso Italia 25, Roma', '345-7654321'),
('BNCLSS92T12A662S', 'Alessia Bianchi', 'Piazza Duomo 5, Napoli', '329-9876543');

-- 2. Officine
INSERT INTO Officina (id_officina, Nome, Indirizzo) VALUES
(1, 'Autofficina Futurista', 'Via Garibaldi 1, Milano'),
(2, 'Officina del Motore', 'Via Nazionale 100, Roma');

-- 3. Staff (collegato a Persona)
INSERT INTO Staff (id_staff, codicefiscale_staff) VALUES
(1, 'RSSMRA80A01H501V'),  -- Mario Rossi
(2, 'VRDLGI85C05F205C');  -- Luigi Verdi

-- 4. Proprietari (collegato a Persona)
INSERT INTO Proprietario (id_proprietario, codicefiscale_proprietario) VALUES
(1, 'BNCLSS92T12A662S');  -- Alessia Bianchi

-- 5. Dipendenti (collegato a Staff)
INSERT INTO Dipendente (id_dipendente, anni_servizio) VALUES
(1, 5);  -- Mario Rossi

-- 6. Direttori (collegato a Staff)
INSERT INTO Direttore (id_direttore, DataNascita) VALUES
(2, '1985-03-05');  -- Luigi Verdi

-- 7. Veicoli
INSERT INTO Veicolo (targa, Modello, Tipo, chilometri) VALUES
('AB123CD', 'Fiat Panda', 'Utilitaria', 50000),
('EF456GH', 'Ford Focus', 'Berlina', 85000);

-- 8. Riparazioni (collegato a Veicolo e Proprietario)
INSERT INTO Riparazione (id_riparazione, Codice, DataAccettazione, OraAccettazione, targa_veicolo, id_proprietario) VALUES
(1, 'RIP-001', '2025-08-10', '10:00:00', 'AB123CD', 1),
(2, 'RIP-002', '2025-08-11', '14:30:00', 'EF456GH', 1);

-- 9. Riparazioni terminate (collegato a Riparazione e Veicolo)
INSERT INTO RiparazioneTerminata (id_riparazione, DataConsegna, OraConsegna, targa_veicolo) VALUES
(1, '2025-08-11', '17:00:00', 'AB123CD');

-- 10. LavoraPresso (collegato a Dipendente e Officina)
INSERT INTO LavoraPresso (id_dipendente, id_officina, inizio_servizio, fine_servizio) VALUES
(1, 1, '2020-01-15', NULL);  -- Mario Rossi lavora nell'officina 1 dal 15/01/2020
