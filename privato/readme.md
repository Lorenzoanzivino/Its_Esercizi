# 🔐 Archivio Credenziali – Guida Completa

Questo documento ti spiega come creare, organizzare e mettere al sicuro il tuo file delle credenziali dentro uno ZIP cifrato AES-256.

---

## 📑 Sommario

- [1. Obiettivo](#1-obiettivo)
- [2. Creazione del file `credenzialitxt`](#2-creazione-del-file-credenzialitxt)
- [3. Struttura consigliata del file](#3-struttura-consigliata-del-file)
- [4. Creazione dello ZIP cifrato AES-256](#4-creazione-dello-zip-cifrato-aes-256)
  - [4.1 Windows (7-Zip)](#41-windows-7-zip)
  - [4.2 Linux / macOS (zip & 7z)](#42-linux--macos-zip--7z)
- [5. Conservazione e backup sicuro](#5-conservazione-e-backup-sicuro)
- [6. Apertura del file dal telefono](#6-apertura-del-file-dal-telefono)
- [7. Regole sulla password dell’archivio](#7-regole-sulla-password-dellarchivio)
- [8. Libro personale delle credenziali](#8-libro-personale-delle-credenziali)
  - [8.1 Social](#81-social)
  - [8.2 Servizi finanziari](#82-servizi-finanziari)
  - [8.3 Dispositivi](#83-dispositivi)
  - [8.4 Account vari](#84-account-vari)
  - [8.5 Codici 2FA e ripristino](#85-codici-2fa-e-ripristino)
  - [8.6 Note personali importanti](#86-note-personali-importanti)
- [9. Checklist finale di sicurezza](#9-checklist-finale-di-sicurezza)
- [10. Struttura dell’archivio ZIP](#10-struttura-dellarchivio-zip)

---

## 🔐 OBIETTIVO

Creare UN file .txt con tutte le tue credenziali →
Metterlo dentro UN archivio .zip cifrato AES-256 →
Conservarlo dove ti pare (PC, telefono, cloud) senza rischiare nulla.

[🔝 Torna su](#-sommario)

---

### 1️⃣ CREA IL FILE DI TESTO (in chiaro)

Fai un file chiamato ad esempio:
```bash
credenziali.txt
```

Strutturalo così (semplice, leggibile):
```bash
=====================
  ACCOUNT PERSONALI
=====================

Gmail
user: lorenzo@example.com
pass: '**************'

Instagram
user: lorenzo.ig
pass: '**************'

=====================
  SERVIZI FINANZIARI
=====================

Banca XYZ
user: lorenzo
pass: '**************'

Carta di credito PIN: '****'
```
Metti ciò che vuoi, è il tuo “quaderno digitale”.

[🔝 Torna su](#-sommario)

---

### 2️⃣ CREA LO ZIP CIFRATO (AES-256)
✔️ Metodo universale (7-Zip — super consigliato)
Windows

- Installa 7-Zip (gratis, open source).

- Tasto destro su credenziali.txt

- 7-Zip → Aggiungi ad archivio…

- Imposta:

    - Formato archivio: zip

    - Metodo cifratura: AES-256

    - Inserisci la password

    - Spunta: “Cifrare nomi file” (importantissimo!)

Clicca OK → otterrai:
```bash
credenziali.zip
```

---

### ✔️ Linux / Mac (terminale)
```bash
zip -e credenziali.zip credenziali.txt
```
⚠️ Nota: zip -e usa cifratura “tradizionale”, non AES.
Per AES-256 devi usare 7z anche su Linux/Mac:
```bash
7z a -tzip credenziali.zip credenziali.txt -mem=AES256
```

[🔝 Torna su](#-sommario)

---

### 3️⃣ CONSERVAZIONE (come fare il backup serio)

Hai 3 posti dove metterlo:

#### ✔️ 1. PC (copia principale)

credenziali.zip sempre aggiornato.

#### ✔️ 2. Chiavetta USB

Una copia di sicurezza.
Se perdi la password → fine, non si apre.

#### ✔️ 3. Cloud (opzionale ma comodo)

Puoi caricare solo il file ZIP cifrato, MAI il txt in chiaro.

Posti sicuri:

  - Google Drive
  - Dropbox
  - OneDrive
  - Mega

Se qualcuno lo ruba → non apre nulla senza password.

[🔝 Torna su](#-sommario)

---

### 4️⃣ COME APRIRLO DAL TELEFONO
Android
Installa:
- ZArchiver
- oppure 7Zipper

Apri → selezioni → inserisci la password → apri il .txt.

iPhone
App consigliata:
- iZip
- Zip & RAR File Extractor

[🔝 Torna su](#-sommario)

---

### 5️⃣ LA COSA PIÙ IMPORTANTE

🔴 La password del tuo ZIP deve essere lunga e NON riutilizzata.
Altrimenti vanifichi tutto.

Esempio buono (da ricordare a memoria):
```bash
Pippo!2024@FarfallaRossa
```
Esempio pessimo:
```bash
123456
lorenzo
password
```

[🔝 Torna su](#-sommario)

---

### LIBRO PERSONALE DELLE CREDENZIALI
```bash
============================================================
                LIBRO PERSONALE DELLE CREDENZIALI
               (Conservare SOLO in archivio cifrato)
============================================================

Ultimo aggiornamento: ________________________


=====================
=  SEZIONE: SOCIAL  =
=====================

GMAIL
  Email: _______________________
  Username: ____________________
  Password: ____________________
  Note: _________________________

INSTAGRAM
  Username: ____________________
  Password: ____________________
  Email recupero: ______________
  Note: _________________________

FACEBOOK
  Email/Username: ______________
  Password: ____________________
  Note: _________________________


==========================
=  SEZIONE: FINANZE      =
==========================

CONTO CORRENTE / BANCA
  Istituto: ____________________
  Username: ____________________
  Password: ____________________
  PIN App: _____________________
  Note: _________________________

CARTA DI CREDITO / DEBITO
  Banca: _______________________
  Numero carta: ________________
  PIN: __________________________
  Password area cliente: _______
  Note: _________________________

PAYPAL
  Email: _______________________
  Password: ____________________
  Note: _________________________


=============================
=  SEZIONE: DISPOSITIVI     =
=============================

PC PRINCIPALE
  Sistema: _____________________
  Utente: ______________________
  Password: ____________________

SMARTPHONE
  Marca/Modello: _______________
  PIN: __________________________
  Password sblocco (se diversa): 
  ______________________________
  Note: _________________________

WIFI CASA
  Nome rete (SSID): ____________
  Password: ____________________
  Note: _________________________


==============================
=  SEZIONE: ACCOUNT VARI     =
==============================

SPOTIFY
  Email: _______________________
  Password: ____________________
  Note: _________________________

NETFLIX
  Email: _______________________
  Password: ____________________
  PIN profilo: _________________
  Note: _________________________

AMAZON
  Email: _______________________
  Password: ____________________
  Note: _________________________


===================================
=  SEZIONE: CODICI E RECUPERI     =
===================================

CODICI 2FA DI RECUPERO
  Servizio: _____________________
  Codici backup:
    - ___________________________
    - ___________________________
    - ___________________________
    - ___________________________
    - ___________________________

CHIAVI DI RIPRISTINO
  Servizio: _____________________
  Chiave: _______________________
  Note: _________________________


===============================
=  NOTE PERSONALI IMPORTANTI  =
===============================
(Annotazioni, informazioni di sicurezza, procedure personali)

_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________


============================================================
              FINE DEL FILE – CONSERVARE IN SICUREZZA
============================================================
```

[🔝 Torna su](#-sommario)

---

### 📌 Checklist rapida (copiala alla fine del file se vuoi)
```bash
[ ] Il file è salvato SOLO in un archivio zip AES-256
[ ] Il file in chiaro NON è più sul desktop o in giro
[ ] Password dell’archivio lunga e non riutilizzata
[ ] Copia dell’archivio su chiavetta USB
[ ] Eventuale copia cloud (solo archivio cifrato)
[ ] Ultimo controllo credenziali effettuato il: ___________
```

[🔝 Torna su](#-sommario)

---

### 📦 STRUTTURA DEL TUO ARCHIVIO ZIP (AES-256)
```bash
credenziali.zip   ← archivio cifrato con password robusta (AES-256)
│
└── Libro_Credenziali.txt   ← il tuo file principale (compilato da te)
```

[🔝 Torna su](#-sommario)
