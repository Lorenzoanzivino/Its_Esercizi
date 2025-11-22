# React_Bibbia.md

## Indice
- [React e ReactDOM](#react-e-reactdom)
- [Componenti e Props](#componenti-e-props)
- [Installazione e Setup](#installazione-e-setup)
- [Variabili in componenti](#variabili-in-componenti)
- [Style Inline](#style-inline)
- [Props approfondimento e spread](#props-approfondimento-e-spread)
- [Iterare liste con map()](#iterare-liste-con-map)
- [Eventi onClick e funzioni](#eventi-onclick-e-funzioni)
- [Callback figlio->padre](#callback-figliopadre)
- [useState](#usestate)
- [useEffect](#useeffect)
- [Forms con useState e useRef](#forms-con-usestate-e-useref)
- [Render condizionali](#render-condizionali)
- [Fetch – chiamate esterne](#fetch--chiamate-esterne)

---

## 🔹 React e ReactDOM

### 🧠 Descrizione breve
**React** costruisce componenti UI; **ReactDOM** serve per montare questi componenti nel DOM del browser.

### ✍️ Tutorial passo-passo
1. Importa React e ReactDOM.
2. Crea un elemento o componente.
3. Usa `createRoot` e `.render()` per inserirlo in `#root`.

### 🧩 Pseudocodice
```text
import react
crea elemento
ottieni root dal DOM
render elemento nel root
```

### 💻 Codice completo
```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';

const elemento = React.createElement('h1', null, 'Ciao React!');
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(elemento);
```

---

## 🔹 Componenti e Props

### 🧠 Descrizione breve
Un componente è una funzione che restituisce JSX. I props sono i suoi parametri immutabili dall'esterno.

### ✍️ Tutorial passo-passo
1. Definisci una function component.
2. Ricevi props come argomento.
3. Rendi il componente riutilizzabile.

### 🧩 Pseudocodice
```text
definisci componente Saluto(props)
  ritorna <h1>Ciao {props.nome}</h1>
usa <Saluto nome='Lorenzo' />
```

### 💻 Codice completo
```jsx
function Saluto({ nome }) {
  return <h1>Ciao {nome}!</h1>;
}

export default Saluto;
```

---

## 🔹 Installazione e Setup

### 🧠 Descrizione breve
Usa `create-react-app` per ottenere un ambiente pronto con Webpack, Babel e dev server.

### ✍️ Tutorial passo-passo
1. `npx create-react-app my-app`
2. `cd my-app` e `npm start`
3. Modifica `src/App.js` e salva: il dev server ricaricherà automaticamente.

### 🧩 Pseudocodice
```text
esegui npx create-react-app
apri progetto
start dev server
scrivi componenti nel src
```

### 💻 Codice completo
```bash
npx create-react-app my-app
cd my-app
npm start
```

---

## 🔹 Variabili in componenti

### 🧠 Descrizione breve
Le variabili locali definiscono valori dinamici e vengono interpolate nel JSX con `{}`.

### ✍️ Tutorial passo-passo
1. Dichiarale all'interno della funzione.
2. Usa `{variabile}` nel JSX.

### 🧩 Pseudocodice
```text
function Comp()
  nome = 'Lorenzo'
  ritorna <p>{nome}</p>
```

### 💻 Codice completo
```jsx
function Info() {
  const nome = 'Lorenzo';
  const eta = 25;
  return <p>{nome} ha {eta} anni.</p>;
}
```

---

## 🔹 Style Inline

### 🧠 Descrizione breve
Gli stili inline sono oggetti JS passati alla prop `style`.

### ✍️ Tutorial passo-passo
1. Crea un oggetto JS con le proprietà in camelCase.
2. Passalo a `<element style={stile}>`.

### 🧩 Pseudocodice
```text
stile = { color: 'red' }
ritorna <p style={stile}>testo</p>
```

### 💻 Codice completo
```jsx
function Titolo() {
  const stile = { color: 'red', fontSize: '18px' };
  return <h2 style={stile}>Titolo</h2>;
}
```

---

## 🔹 Props approfondimento e spread

### 🧠 Descrizione breve
I props sono un oggetto immutabile passato dal genitore; lo spread permette di passarne molti velocemente.

### ✍️ Tutorial passo-passo
1. Destruttura i props direttamente nella firma della funzione.
2. Usa `{...obj}` per passare tutte le proprietà.

### 🧩 Pseudocodice
```text
props = {nome, eta}
<Profilo {...props} />
```

### 💻 Codice completo
```jsx
function Profilo({ nome, eta }) {
  return <p>{nome} - {eta}</p>;
}

const dati = { nome: 'Lorenzo', eta: 25 };
<Profilo {...dati} />;
```

---

## 🔹 Iterare liste con map

### 🧠 Descrizione breve
`map()` genera una lista di elementi JSX da un array di dati. Ogni elemento necessita di una `key` unica.

### ✍️ Tutorial passo-passo
1. Prepara un array di dati.
2. Usa `array.map(item => <Componente key={id} ... />)`.

### 🧩 Pseudocodice
```text
for ogni elemento in array
  crea <li key=index>elemento</li>
ritorna <ul>lista</ul>
```

### 💻 Codice completo
```jsx
function ListaUtenti({ users }) {
  return (
    <ul>
      {users.map(u => <li key={u.id}>{u.name}</li>)}
    </ul>
  );
}
```

---

## 🔹 Eventi onClick e funzioni

### 🧠 Descrizione breve
Gli eventi si passano come funzioni alla prop `onClick`. Non invocare la funzione durante il render (es. `onClick={f}` non `onClick={f()}`).

### ✍️ Tutorial passo-passo
1. Definisci una funzione handler.
2. Passala a `onClick={handler}`.
3. Se vuoi passare argomenti usa arrow function: `onClick={() => handler(arg)}`.

### 🧩 Pseudocodice
```text
function handler(param)
  fai qualcosa
<button onClick={() => handler(x)} />
```

### 💻 Codice completo
```jsx
function Saluto() {
  function handleClick(nome) {
    alert(`Ciao ${nome}`);
  }
  return <button onClick={() => handleClick('Lorenzo')}>Saluta</button>;
}
```

---

## 🔹 Callback (Figlio → Padre)

### 🧠 Descrizione breve
Per passare dati dal figlio al padre, il padre passa una funzione al figlio via props; il figlio chiama quella funzione.

### ✍️ Tutorial passo-passo
1. Il padre definisce `handleFromChild`.
2. Passa `handleFromChild` come prop al figlio.
3. Il figlio invoca la funzione con i dati.

### 🧩 Pseudocodice
```text
padre.handle = funzione che riceve dato
<Figlio onSend={padre.handle} />
Figlio: props.onSend(dato)
```

### 💻 Codice completo
```jsx
function Figlio({ onSend }) {
  return <button onClick={() => onSend('ping')}>Invia al padre</button>;
}

function Padre() {
  function ricevi(msg) {
    console.log('Ricevuto:', msg);
  }
  return <Figlio onSend={ricevi} />;
}
```

---

## 🔹 useState

### 🧠 Descrizione breve
`useState` è un hook che fornisce uno stato locale al componente e una funzione per aggiornarlo.

### ✍️ Tutorial passo-passo
1. Importa `useState`.
2. Inizializza: `const [state, setState] = useState(initial)`.
3. Aggiorna con `setState(newValue)` o callback `setState(prev => ...)`.

### 🧩 Pseudocodice
```text
count = useState(0)
button onClick => setCount(count+1)
```

### 💻 Codice completo
```jsx
import { useState } from 'react';
function Counter() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <p>{count}</p>
      <button onClick={() => setCount(prev => prev + 1)}>+</button>
    </div>
  );
}
```

---

## 🔹 useEffect

### 🧠 Descrizione breve
`useEffect` gestisce effetti collaterali: chiamate fetch, subscribe a eventi, timers. Si esegue dopo il render.

### ✍️ Tutorial passo-passo
1. Importa `useEffect`.
2. `useEffect(() => { ... }, [deps])`.
3. Return opzionale per cleanup.

### 🧩 Pseudocodice
```text
useEffect(() => {
  subscribe event
  return () => unsubscribe
}, [deps])
```

### 💻 Codice completo
```jsx
import { useEffect, useState } from 'react';
function WindowSize() {
  const [size, setSize] = useState({ w: window.innerWidth, h: window.innerHeight });
  useEffect(() => {
    function onResize() {
      setSize({ w: window.innerWidth, h: window.innerHeight });
    }
    window.addEventListener('resize', onResize);
    return () => window.removeEventListener('resize', onResize);
  }, []);
  return <div>W: {size.w} H: {size.h}</div>;
}
```

---

## 🔹 Forms con useState e useRef

### 🧠 Descrizione breve
- `useState`: form controllati (binding valore <-> stato).
- `useRef`: form non controllati, accesso diretto al DOM.

### ✍️ Tutorial passo-passo
1. Per controllati: `value={state}` e `onChange` aggiorna lo stato.
2. Per non controllati: usa `ref` e leggi `ref.current.value`.

### 🧩 Pseudocodice
```text
// controllato
state = ''
<input value=state onChange=aggiorna />

// non controllato
ref = useRef()
<input ref=ref />
button onClick => console.log(ref.current.value)
```

### 💻 Codice completo
```jsx
import { useRef, useState } from 'react';

function FormControllato() {
  const [val, setVal] = useState('');
  return (
    <form onSubmit={(e) => e.preventDefault()}>
      <input value={val} onChange={e => setVal(e.target.value)} />
      <p>Valore: {val}</p>
    </form>
  );
}

function FormNonControllato() {
  const inputRef = useRef();
  return (
    <>
      <input ref={inputRef} />
      <button onClick={() => alert(inputRef.current.value)}>Leggi</button>
    </>
  );
}
```

---

## 🔹 Render Condizionali

### 🧠 Descrizione breve
Mostrare o nascondere UI in base a condizioni: `if`, ternario, short-circuit.

### ✍️ Tutorial passo-passo
1. Calcola la condizione.
2. Usa `if` fuori dal JSX o `? / :` dentro JSX.

### 🧩 Pseudocodice
```text
if logged => mostra logout
else => mostra login
```

### 💻 Codice completo
```jsx
function Access({ isLoggedIn }) {
  if (!isLoggedIn) return <button>Login</button>;
  return <button>Logout</button>;
}

function Messaggio({ isAdmin }) {
  return <div>{isAdmin ? 'Admin' : 'User'}</div>;
}
```

---

## 🔹 Fetch – chiamate esterne

### 🧠 Descrizione breve
Usa `fetch` per recuperare risorse esterne. Spesso combinato con `useEffect` per caricare dati al montaggio.

### ✍️ Tutorial passo-passo
1. Nel `useEffect` fai `fetch(url)`.
2. `.then(res => res.json())` e aggiorna stato.
3. Gestisci loading ed errori.

### 🧩 Pseudocodice
```text
on mount => set loading true
fetch url
if ok => set dati, loading false
if error => set error
```

### 💻 Codice completo
```jsx
import { useEffect, useState } from 'react';

function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/users')
      .then(res => {
        if (!res.ok) throw new Error('Network response was not ok');
        return res.json();
      })
      .then(data => setUsers(data))
      .catch(err => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Caricamento...</p>;
  if (error) return <p>Errore: {error}</p>;

  return (
    <ul>
      {users.map(u => <li key={u.id}>{u.name}</li>)}
    </ul>
  );
}
```

---

# Fine file React_Bibbia
