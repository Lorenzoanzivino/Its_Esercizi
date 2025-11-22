# eBuy - Sistema di gestione aste online

**Modulo**: Progettazione, Basi di Dati  
**Professore**: Toni Mancini  
**ICT Academy** - Versione 2024-09-01

---

## 📚 Indice

1. [Introduzione](#introduzione)
2. [Requisiti funzionali](#requisiti-funzionali)
3. [Diagrammi UML](#diagrammi-uml)
4. [Specifiche delle classi](#specifiche-delle-classi)
5. [Operazioni principali](#operazioni-principali)
6. [Tecnologie utilizzate](#tecnologie-utilizzate)
7. [Autore e collaboratori](#autore-e-collaboratori)

---

## 📝 Introduzione

**eBuy** è un sistema informatico progettato per la gestione di aste online e attività di commercio elettronico. Il sistema consente agli utenti registrati di:

- Pubblicare annunci per la vendita di oggetti.
- Gestire aste al rialzo per l'aggiudicazione degli oggetti.
- Vendere oggetti senza asta (modalità "compralo subito").

L'applicazione supporta sia utenti privati che venditori professionali, con funzionalità per pubblicare oggetti, fare offerte, e acquistare articoli. Inoltre, il sistema include meccanismi di feedback e di calcolo dell'affidabilità dei venditori.

---

## 📋 Requisiti funzionali

### **Gestione degli utenti**
- **Utenti registrati**: Ogni utente ha un nome scelto e una data di registrazione.
- **Tipi di utenti**: Privati e venditori professionali. Solo gli utenti privati possono fare offerte (bid) e acquistare articoli.

### **Gestione dei post (annunci di vendita)**
Ogni post contiene:
- **Descrizione dell'oggetto**: Dettagli sull'oggetto in vendita.
- **Categoria**: La categoria dell'oggetto (es. elettronica, abbigliamento, etc.).
- **Prezzo di vendita**: Prezzo base dell'oggetto.
- **Metodo di pagamento**: Bonifico o carta di credito.
- **Condizione**: Oggetto nuovo o usato.

I post sono di due tipi:
1. **Asta**: Vendita tramite asta al rialzo (con prezzo iniziale e rialzo per offerta).
2. **Compralo subito**: Vendita immediata senza asta (prezzo fisso).

### **Gestione delle offerte (bid)**
- Un utente può fare un'offerta per un oggetto in vendita tramite asta.
- L'offerta aumenta il prezzo dell'oggetto di una quantità predefinita (rialzo).
- L'asta si conclude automaticamente alla data/ora prestabilita.

### **Feedback e affidabilità dei venditori**
- Ogni transazione può essere valutata tramite un **feedback** numerico (0-5).
- L'affidabilità di un venditore è calcolata sulla base dei feedback ricevuti, con penalizzazioni per feedback negativi.

### **Venditori professionali**
- I venditori professionali hanno una **vetrina online** (URL) e pubblicano informazioni legali aggiuntive.
- La popolarità del venditore professionale è calcolata in base al numero di bid e acquisti degli utenti negli ultimi 12 mesi.

---

## 📐 Diagrammi UML

### **UML delle Classi**
Il diagramma delle classi descrive le entità principali del sistema, tra cui:
- **Utente**: Gestisce le informazioni dell'utente (privato o venditore).
- **Post**: Rappresenta un annuncio di vendita, che può essere di tipo asta o compralo subito.
- **Offerta (Bid)**: Descrive un'offerta fatta da un utente per un oggetto in asta.
- **Feedback**: Rappresenta la valutazione lasciata da un acquirente su un venditore.

*Il diagramma UML delle classi può essere creato utilizzando strumenti come VisualParadigm.*

### **UML degli Use-Case**
Il diagramma degli use-case descrive le interazioni tra gli utenti e il sistema:
- **Pubblicare un post**.
- **Fare un'offerta** (bid) per un'asta.
- **Acquistare un oggetto con "compralo subito"**.
- **Lasciare un feedback**.

---

## 🧑‍💻 Specifiche delle classi

### **Classe Utente**
- **Attributi**:
  - `nome`: stringa (Nome scelto dall'utente).
  - `dataRegistrazione`: data (Data di registrazione dell'utente).
  - `tipo`: stringa (Privato o Venditore Professionale).
  
### **Classe Post**
- **Attributi**:
  - `titolo`: stringa (Nome dell'oggetto).
  - `descrizione`: stringa (Descrizione dell'oggetto).
  - `categoria`: stringa (Categoria dell'oggetto).
  - `prezzo`: float (Prezzo dell'oggetto).
  - `metodoPagamento`: stringa (Bonifico o Carta di credito).
  - `condizione`: stringa (Nuovo o Usato).
  - `tipologia`: stringa (Asta o Compralo subito).
  - `dataScadenza`: data (Data di scadenza dell'asta, se applicabile).
  - `rialzo`: float (Ammontare del rialzo, se applicabile).
  
### **Classe Offerta (Bid)**
- **Attributi**:
  - `utente`: stringa (Nome dell'utente che ha fatto l'offerta).
  - `importo`: float (Importo dell'offerta).
  - `dataOfferta`: data (Data in cui è stata effettuata l'offerta).
  
### **Classe Feedback**
- **Attributi**:
  - `voto`: int (Voto numerico da 0 a 5).
  - `commento`: stringa (Commento facoltativo).
  - `dataFeedback`: data (Data di rilascio del feedback).

---

## 🏆 Operazioni principali

### **Pubblicazione di un post**
Un utente può pubblicare un post per un oggetto in vendita:
- Se l'oggetto è venduto tramite asta, deve specificare il prezzo iniziale, il rialzo e la scadenza.
- Se l'oggetto è venduto tramite la modalità "compralo subito", deve solo specificare il prezzo.

### **Fare un'offerta (bid)**
Un utente può fare un'offerta per un oggetto in asta:
- L'importo dell'offerta è uguale all'ultimo prezzo più il rialzo.
- Se l'offerta è valida, diventa l'offerta più alta.

### **Acquisto "compralo subito"**
Un utente può acquistare un oggetto al prezzo fisso, senza l'asta:
- L'oggetto è venduto immediatamente al primo utente che acquista.

### **Lasciare un feedback**
Dopo una transazione, l'acquirente può lasciare un feedback numerico per il venditore:
- Il feedback è usato per calcolare l'affidabilità del venditore.

### **Calcolo dell'affidabilità**
L'affidabilità di un venditore è calcolata come la media dei feedback ricevuti, con penalizzazione per i feedback negativi.

---

## ⚙️ Tecnologie utilizzate

- **Java**: Linguaggio di programmazione per la logica di backend.
- **Spring Boot**: Framework per la gestione delle API.
- **MySQL**: Database relazionale per la memorizzazione dei dati.
- **VisualParadigm**: Strumento per la creazione dei diagrammi UML.
- **JUnit**: Framework per i test unitari.

---

## 🧑‍💻 Autore e collaboratori

**Autore**: [Tuo Nome]  
**Collaboratori**: Toni Mancini  
**ICT Academy**

---

**Nota**: Questo README è una descrizione generale del progetto **eBuy**, con focus sui requisiti, la struttura delle classi e le operazioni principali del sistema. Può essere usato come base per l'implementazione del sistema.

