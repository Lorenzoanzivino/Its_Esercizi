# JavaScript Avanzato e Introduzione a React  
## (Parte 2 — dal punto 5 al punto 21)

---

## 5 — Node.js

### Cos’è
Node.js è un **runtime JavaScript** per eseguire codice JS **fuori dal browser**, cioè lato server.  
Permette di lavorare con:
- File system
- Server HTTP
- Moduli (import/export)
- Processi, eventi, stream...

### Differenze tra Browser e Node.js

| Aspetto | Browser | Node.js |
|----------|----------|----------|
| Ambiente globale | `window` | `global` |
| Accesso DOM | ✅ | ❌ |
| API di rete (fetch, document, ecc.) | ✅ | ❌ |
| File system | ❌ | ✅ |
| Moduli | ES Modules | CommonJS + ES Modules |

### Installazione
1. Scarica da [https://nodejs.org](https://nodejs.org) (versione LTS).
2. Verifica:
   ```bash
   node -v
   npm -v
   ```
3. npm (Node Package Manager) serve per installare pacchetti.

---

## 6 — Prima Pagina React

### React vs ReactDOM
React: si occupa della logica e dei componenti.  
ReactDOM: si occupa del render nel browser.

### Creazione elemento manuale (senza JSX)
```js
const elemento = React.createElement('h1', null, 'Ciao React!');
ReactDOM.render(elemento, document.getElementById('root'));
```

**JSX** è solo zucchero sintattico: viene trasformato in `React.createElement()` dal compilatore (Babel).

### Virtual DOM
React non manipola direttamente il DOM reale, ma usa una rappresentazione virtuale (Virtual DOM) che confronta e aggiorna solo ciò che è cambiato → più performance.

---

## 7 — Componenti e Props

### Cos’è un componente
È una funzione (o classe) che restituisce elementi UI.
```js
function Saluto() {
  return <h1>Ciao mondo!</h1>;
}
```

### Props (proprietà)
```js
function Saluto(props) {
  return <h2>Ciao, {props.nome}</h2>;
}

<Saluto nome="Lorenzo" />;
```

---

## 8 — Installazione dell’Ambiente React (SPA)

### Passaggi
1. Installa Node.js e npm.
2. Crea un progetto React:
   ```bash
   npx create-react-app mia-app
   cd mia-app
   npm start
   ```
3. Struttura base:
   - `src/` → codice React
   - `App.js` → componente principale
   - `index.js` → punto di ingresso
   - `public/` → file statici

---

## 9 — Variabili in un Componente

```js
function Info() {
  const nome = "Lorenzo";
  const corso = "Cloud Developer";

  return <p>Ciao {nome}, benvenuto nel corso {corso}!</p>;
}
```

Usiamo `{}` per inserire valori JS nel JSX.

---

## 10 — Style Inline

```js
const stile = { color: 'red', fontSize: '18px' };

function Titolo() {
  return <h1 style={stile}>Ciao React!</h1>;
}
```

**Nota:** le proprietà CSS diventano camelCase → `backgroundColor`, `textAlign` ecc.

---

## 11 — Approfondimento sui Props

```js
function Persona({ nome, eta }) {
  return <p>{nome} ha {eta} anni.</p>;
}

function App() {
  return (
    <div>
      <Persona nome="Lorenzo" eta={23} />
      <Persona nome="Marco" eta={30} />
    </div>
  );
}
```

---

## 12 — Passare parametri con lo Spread Operator

```js
const dati = { nome: "Lorenzo", eta: 23 };

function Persona({ nome, eta }) {
  return <p>{nome} ha {eta} anni.</p>;
}

function App() {
  return <Persona {...dati} />;
}
```

---

## 13 — Iterare una lista in JSX con map()

```js
const studenti = ["Lorenzo", "Marco", "Giulia"];

function App() {
  return (
    <ul>
      {studenti.map((nome, i) => <li key={i}>{nome}</li>)}
    </ul>
  );
}
```

Ogni elemento deve avere una `key` univoca.

---

## 14 — Gestione evento onClick

```js
function Bottone() {
  function saluta() {
    alert("Ciao!");
  }
  return <button onClick={saluta}>Cliccami</button>;
}
```

> ⚠️ Attenzione: `onClick={saluta}` passa la funzione.  
> `onClick={saluta()}` la invoca subito.

---

## 15 — Funzioni e Eventi con Parametri

```js
function Bottone() {
  function mostraMessaggio(nome) {
    alert("Ciao " + nome);
  }
  return <button onClick={() => mostraMessaggio("Lorenzo")}>Saluta</button>;
}
```

---

## 16 — Callback Function (Figlio → Padre)

```js
function Figlio({ onInvia }) {
  return <button onClick={() => onInvia("Messaggio dal figlio!")}>Invia</button>;
}

function Padre() {
  function ricevi(msg) {
    console.log(msg);
  }
  return <Figlio onInvia={ricevi} />;
}
```

---

## 17 — useState: Gestione dello Stato

```js
import { useState } from "react";

function Contatore() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <p>Hai cliccato {count} volte</p>
      <button onClick={() => setCount(count + 1)}>Aumenta</button>
    </div>
  );
}
```

---

## 18 — useState con Stringhe, Array e Oggetti

```js
// Stringa
const [nome, setNome] = useState("Lorenzo");
setNome("Marco");

// Array
const [lista, setLista] = useState(["A", "B"]);
setLista([...lista, "C"]);

// Oggetto
const [utente, setUtente] = useState({ nome: "Lorenzo", eta: 23 });
setUtente({ ...utente, eta: 24 });
```

---

## 19 — useEffect

```js
import { useEffect, useState } from "react";

function Timer() {
  const [secondi, setSecondi] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => setSecondi(s => s + 1), 1000);
    return () => clearInterval(interval);
  }, []);

  return <p>Tempo: {secondi}s</p>;
}
```

---

## 20 — Form con useState

```js
import { useState } from "react";

function Form() {
  const [nome, setNome] = useState("");

  function handleSubmit(e) {
    e.preventDefault();
    alert("Hai inserito: " + nome);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input value={nome} onChange={(e) => setNome(e.target.value)} />
      <button type="submit">Invia</button>
    </form>
  );
}
```

---

## 21 — Render Condizionali

### Con if
```js
function Messaggio({ loggato }) {
  if (loggato) return <p>Benvenuto!</p>;
  return <p>Effettua il login.</p>;
}
```

### Operatore ternario
```js
{loggato ? <p>Benvenuto!</p> : <p>Accedi</p>}
```

### Short-circuit (&&)
```js
{loggato && <p>Benvenuto!</p>}
```

---

## 22 — Fetch (cenno)

```js
import { useEffect, useState } from "react";

function Utenti() {
  const [utenti, setUtenti] = useState([]);

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then(res => res.json())
      .then(data => setUtenti(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <ul>
      {utenti.map(u => <li key={u.id}>{u.name}</li>)}
    </ul>
  );
}
```

### 🔍 Suggerimenti Finali

    - Non modificare mai lo stato direttamente (state.prop = ... ❌).

    - Usa sempre setState o funzioni aggiornate (prev => ...).

    - Ogni elemento di una lista ha bisogno di key.

    - Gestisci gli effetti collaterali con useEffect.

    - React è dichiarativo: descrivi cosa vuoi ottenere, non come farlo.