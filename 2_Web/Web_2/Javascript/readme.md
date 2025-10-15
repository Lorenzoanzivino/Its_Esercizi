# JavaScript_Avanzato.md

## Indice
- [Oggetti JavaScript](#oggetti-javascript)
- [Funzioni Costruttore](#funzioni-costruttore)
- [Destructuring (Destrutturazione)](#destructuring-destrutturazione)
- [Spread Operator (...)](#spread-operator-)
- [Node.js (introduzione)](#nodejs-introduzione)

---

## 🔹 Oggetti JavaScript

### 🧠 Descrizione breve
Un oggetto in JavaScript è una collezione di coppie chiave-valore: proprietà (valori) e metodi (funzioni). Gli oggetti sono fondamentali per modellare dati complessi.

### ✍️ Tutorial passo-passo
1. Creazione: usa la sintassi letterale `{}` o il costruttore `new Object()`.
2. Aggiungere/modificare proprietà: `obj.prop = value` o `obj['prop'] = value`.
3. Metodi: assegna una funzione a una proprietà.
4. Iterare: `for...in`, `Object.keys()`, `Object.entries()`.

### 🧩 Pseudocodice
```text
crea oggetto persona con nome e età
leggi persona.nome
modifica persona.eta
chiama persona.saluta() che stampa un messaggio
```

### 💻 Codice completo
```js
// creazione e manipolazione
const persona = { nome: 'Lorenzo', eta: 25 };
persona.citta = 'Roma';

// proprietà e metodo
persona.saluta = function() {
  return `Ciao, sono ${this.nome} e ho ${this.eta} anni.`;
};

console.log(persona.saluta());

// accesso con notazione a quadre (utile per chiavi dinamiche)
const chiave = 'citta';
console.log(persona[chiave]);

// iterazione
for (const k in persona) {
  console.log(k, persona[k]);
}

console.log(Object.keys(persona));
console.log(Object.entries(persona));
```

---

## 🔹 Funzioni Costruttore

### 🧠 Descrizione breve
Le constructor function (funzioni costruttrici) sono pattern per creare oggetti simili (istanze) usando la keyword `new` e `this` per assegnare proprietà.

### ✍️ Tutorial passo-passo
1. Definisci una funzione con la convenzione PascalCase.
2. All'interno usa `this.prop = value`.
3. Aggiungi metodi al prototype per risparmiare memoria.
4. Istanzia con `new NomeFunzione(args)`.

### 🧩 Pseudocodice
```text
definisci Costruttore Persona(nome, eta)
  this.nome = nome
  this.eta = eta
Persona.prototype.saluta = funzione che stampa nome e eta
crea istanza p = new Persona('Lorenzo', 25)
chiama p.saluta()
```

### 💻 Codice completo
```js
function Persona(nome, eta) {
  this.nome = nome;
  this.eta = eta;
}

Persona.prototype.saluta = function() {
  console.log(`Ciao, sono ${this.nome} e ho ${this.eta} anni.`);
};

const p = new Persona('Lorenzo', 25);
p.saluta();

// ES6 class (sintassi sugar)
class PersonaClass {
  constructor(nome, eta) {
    this.nome = nome;
    this.eta = eta;
  }
  saluta() {
    console.log(`Ciao, sono ${this.nome}`);
  }
}
const pc = new PersonaClass('Anna', 30);
pc.saluta();
```

---

## 🔹 Destructuring (Destrutturazione)

### 🧠 Descrizione breve
Il destructuring permette di estrarre valori da array o oggetti in variabili separate con sintassi concisa.

### ✍️ Tutorial passo-passo
- Per gli array: `[a, b] = arr` prende i primi elementi.
- Per gli oggetti: `{x, y} = obj` prende le proprietà con quei nomi.
- Puoi dare valori di default e rinominare variabili.

### 🧩 Pseudocodice
```text
dato array [1,2,3]
assegna a = 1, b = 2
dato object {nome: 'L', eta:25}
assegna nome, eta a variabili
```

### 💻 Codice completo
```js
// array
const arr = [10, 20, 30];
const [a, b, ...rest] = arr; // a=10, b=20, rest=[30]

// oggetto
const obj = { nome: 'Lorenzo', eta: 25, citta: 'Roma' };
const { nome, eta, citta: città } = obj; // rinomina citta -> città

// default values
const { ruolo = 'studente' } = obj;

console.log(a, b, rest, nome, eta, città, ruolo);
```

---

## 🔹 Spread Operator (...)

### 🧠 Descrizione breve
Lo spread `...` espande elementi di array o proprietà di oggetti. È utile per clonare, unire e passare argomenti.

### ✍️ Tutorial passo-passo
- Array: `newArr = [...arr1, ...arr2]`
- Oggetti: `newObj = { ...obj1, extra: 1 }`
- Differenza da rest: spread espande, rest raccoglie in una variabile.

### 🧩 Pseudocodice
```text
dato arr1 e arr2
crea arr3 che contiene elementi di arr1 seguiti arr2
dato obj1
crea obj2 che copia obj1 e aggiunge una proprietà
```

### 💻 Codice completo
```js
const arr1 = [1,2];
const arr2 = [3,4];
const arr3 = [...arr1, ...arr2];

const obj1 = { a: 1, b: 2 };
const obj2 = { ...obj1, c: 3 };

function somma(x, y, z) { return x + y + z; }
const nums = [1,2,3];
console.log(somma(...nums));

console.log(arr3, obj2);
```

---

## 🔹 Node.js (introduzione)

### 🧠 Descrizione breve
Node.js è un runtime che permette di eseguire JavaScript lato server. Fornisce moduli built-in (fs, http) e package tramite npm.

### ✍️ Tutorial passo-passo
1. Scarica e installa Node.js dal sito ufficiale.
2. Verifica con `node -v` e `npm -v`.
3. Inizia un progetto `npm init -y` e installa pacchetti `npm i express`.
4. Differenze: ambiente senza DOM, moduli CommonJS/ESM, accesso file system.

### 🧩 Pseudocodice
```text
installa node
crea file server.js
require express
crea app che risponde GET /
ascolta porta 3000
```

### 💻 Codice completo
```js
// server.js - esempio con express
const express = require('express');
const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
  res.send('Ciao dal server Node.js!');
});

app.listen(PORT, () => console.log(`Server ascolta su http://localhost:${PORT}`));
```

---

# Fine file JavaScript_Avanzato
