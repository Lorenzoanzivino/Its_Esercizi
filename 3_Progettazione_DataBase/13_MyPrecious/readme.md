# 📜 Progetto: MyPrecious - Sistema di gestione opere d'arte e esposizioni

**Modulo**: Progettazione 1  
**Esame**: Prova B  
**Data**: 21 novembre 2024  
**Docenti**: Toni Mancini, Marco Esposito  
**Accademia**: ITS ICT Academy

---

## 📚 Indice

1. [Descrizione del progetto](#descrizione-del-progetto)
2. [Requisiti funzionali](#requisiti-funzionali)
3. [Diagrammi UML](#diagrammi-uml)
4. [Specifiche delle classi](#specifiche-delle-classi)
5. [Operazioni di Use-Case](#operazioni-di-use-case)
6. [Tecnologie utilizzate](#tecnologie-utilizzate)
7. [Autore e collaboratori](#autore-e-collaboratori)

---

## 📖 Descrizione del progetto

Il sistema **MyPrecious** è destinato alla gestione delle opere d'arte e delle esposizioni per conto di un museo. Il sistema permette ai responsabili del museo di gestire il patrimonio artistico, organizzare esposizioni permanenti e temporanee, e raccogliere statistiche sulle visite e vendite dei biglietti.

### Obiettivi principali:
- Gestire opere d'arte e informazioni su artisti e esposizioni.
- Organizzare esposizioni, permanenti e temporanee, con diverse tariffe di biglietti.
- Monitorare le vendite di biglietti e generare report sui guadagni.

---

## 📋 Requisiti funzionali

### **Gestione Opere d'arte**
Ogni opera d'arte è descritta da:
- **Nome**: Titolo dell'opera.
- **Categoria**: Tipo di opera (es. dipinto, scultura, mosaico, manoscritto).
- **Autore**: L'artista che ha creato l'opera.
- **Anno di realizzazione**: Anno di produzione.
- **Tecnica**: Descrizione della tecnica usata (se rilevante).
- **Corrente artistica**: Appartenenza a correnti artistiche (es. Rinascimento, Barocco).

### **Gestione Artisti**
Ogni artista ha:
- **Nome d'arte**: Nome dell'artista.
- **Luogo e data di nascita**.
- **Data di morte** (se applicabile).
- **Opere**: Elenco delle opere possedute dal museo.

### **Gestione Esposizioni**
Le esposizioni possono essere:
- **Permanenti**: Mostre sempre attive con le opere più importanti.
- **Temporanee**: Esposizioni a tema con durata limitata e prezzi variabili.

Le esposizioni temporanee includono:
- **Nome**.
- **Periodo**: Inizio e fine della mostra.
- **Prezzo d'accesso**: Tariffa per accedere all'esposizione.

### **Gestione Biglietti**
I biglietti possono essere di due tipi:
- **Standard**: Accesso solo alle esposizioni permanenti.
- **Extended access**: Accesso alle esposizioni permanenti e una selezione di esposizioni temporanee a scelta.

Ogni biglietto ha:
- **Tariffa scelta**.
- **Istante di vendita**.
- **Data di validità** scelta dal visitatore.

---

## 🏗️ Diagrammi UML

### **UML delle Classi**
Il diagramma delle classi descrive le relazioni tra le entità principali del sistema, inclusi **Opere**, **Artisti**, **Esposizioni**, **Biglietti** e **Tariffe**.

*Il diagramma è stato creato utilizzando VisualParadigm, e include tutte le classi e le loro interazioni.*

### **UML degli Use-Case**
Il diagramma degli use-case descrive le interazioni tra gli utenti (responsabili del museo) e il sistema **MyPrecious**. Le funzionalità principali includono:
- Aggiungere/Modificare/Rimuovere opere.
- Creare/Modificare esposizioni.
- Registrare la vendita di biglietti.
- Calcolare i guadagni delle esposizioni temporanee.

---

## 🧑‍💻 Specifica delle classi

### **Classe Opera**
- **Attributi**:
  - `nome`: stringa (Nome dell'opera).
  - `categoria`: stringa (Categoria dell'opera).
  - `autore`: autore (Collegamento con l'artista).
  - `annoRealizzazione`: int (Anno di realizzazione).
  - `tecnica`: stringa (Tecnica utilizzata).
  - `correnteArtistica`: stringa (Corrente artistica associata).
  
### **Classe Artista**
- **Attributi**:
  - `nomeArte`: stringa (Nome dell'artista).
  - `luogoNascita`: stringa (Luogo di nascita).
  - `dataNascita`: data (Data di nascita).
  - `dataMorte`: data (Data di morte, se applicabile).
  - `opere`: lista di opere (Opere create dall'artista e di proprietà del museo).

### **Classe Esposizione**
- **Attributi**:
  - `nome`: stringa (Nome dell'esposizione).
  - `tipo`: stringa (Permanente o Temporanea).
  - `periodo`: intervallo di date (Date di inizio e fine esposizione).
  - `prezzoAccesso`: float (Prezzo di accesso per esposizione temporanea).
  - `opereEsposte`: lista di opere (Opere esposte durante l'esposizione).

---

## 💻 Operazioni di Use-Case

### **Vendita Biglietto**
- **Descrizione**: Registrare la vendita di un biglietto.
- **Operazioni**:
  - Selezionare la tariffa del biglietto.
  - Calcolare il prezzo in base alla tipologia di biglietto (Standard o Extended access).
  - Associare il biglietto a una data di validità.

### **Calcolo Introiti**
- **Descrizione**: Calcolare gli introiti generati dalle esposizioni temporanee.
- **Operazioni**:
  - Dato un periodo, sommare i guadagni dei biglietti venduti.

### **Statistica Biglietti Extended Access**
- **Descrizione**: Calcolare il numero di biglietti di tipo **Extended access** venduti per una data esposizione in un periodo specifico.
- **Operazioni**:
  - Filtrare i biglietti venduti per tipo e periodo.
  - Restituire il totale dei biglietti venduti per esposizione temporanea.

---

## ⚙️ Tecnologie utilizzate

- **Java** (per la logica di backend)
- **Spring Boot** (per la gestione delle API)
- **MySQL** (per la gestione del database)
- **VisualParadigm** (per la creazione dei diagrammi UML)
- **JUnit** (per i test unitari)

---

## 🧑‍💻 Autore e collaboratori

**Autore**: [Tuo Nome]  
**Collaboratori**: Toni Mancini, Marco Esposito  
**ITS ICT Academy - Cloud Developer**

---

**Nota**: Questo README descrive solo le operazioni e i diagrammi richiesti dal progetto, e include la definizione delle classi, le specifiche delle operazioni di Use-Case e le tecnologie utilizzate.

