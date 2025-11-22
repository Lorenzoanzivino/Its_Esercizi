# 📖 JavaScript Promises

## Cos’è una Promise

Una **Promise** è un **oggetto che rappresenta il risultato di un’operazione asincrona** che **potrebbe non essere ancora completata**. È come una promessa: il codice dice “ti darò un risultato in futuro” e puoi decidere **cosa fare quando sarà pronto**.

### Stati di una Promise

1. **Pending (in sospeso)** → operazione in corso  
2. **Fulfilled (risolta)** → operazione completata con successo (`resolve`)  
3. **Rejected (rifiutata)** → operazione fallita (`reject`)  

---

## Creare una Promise

```javascript
const myPromise = new Promise((resolve, reject) => {
    let successo = true; // esempio
    if (successo) {
        resolve("Operazione completata!");
    } else {
        reject("Qualcosa è andato storto.");
    }
});
```

---

## Funzione che restituisce una Promise

```javascript
function caricaDati() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const successo = true;
            if (successo) {
                resolve({ nome: "Lorenzo", ruolo: "Developer" });
            } else {
                reject("Errore nel caricamento dati");
            }
        }, 2000);
    });
}

caricaDati()
    .then((dati) => console.log("Dati caricati:", dati))
    .catch((err) => console.error(err));
```

---

## Consumo di Promise

- `.then()` → gestisce il successo (`resolve`)  
- `.catch()` → gestisce l’errore (`reject`)  
- `.finally()` → esegue codice comunque, successo o fallimento  

```javascript
myPromise
    .then(result => console.log("Successo:", result))
    .catch(error => console.error("Errore:", error))
    .finally(() => console.log("Operazione completata"));
```

---

## Chaining di Promise

```javascript
new Promise(resolve => resolve(5))
    .then(x => x + 1)  // 6
    .then(x => x * 2)  // 12
    .then(x => console.log(x)); // stampa 12
```

---

## Async/Await

```javascript
async function mostraDati() {
    try {
        const dati = await caricaDati();
        console.log("Dati ricevuti:", dati);
    } catch (err) {
        console.error("Errore:", err);
    } finally {
        console.log("Operazione terminata");
    }
}

mostraDati();
```

- `await` → aspetta che la Promise venga risolta o rifiutata  
- `async` → indica che la funzione ritorna una Promise  
- Errori → gestiti con `try/catch`  

---

## Promise combinator

- `Promise.all(array)` → tutte le Promise devono risolversi, se una fallisce fallisce tutto  
- `Promise.allSettled(array)` → aspetta tutte le Promise e ti dice chi ha avuto successo e chi no  
- `Promise.race(array)` → prende il risultato della prima Promise che si risolve o fallisce  
- `Promise.any(array)` → prende il risultato della prima Promise **risolta**, ignora i fallimenti  

```javascript
const p1 = Promise.resolve(10);
const p2 = new Promise(resolve => setTimeout(() => resolve(20), 1000));

Promise.all([p1, p2])
    .then(console.log) // [10, 20]
    .catch(console.error);
```

---

## Best Practice

1. **Non annidare troppe callback** → preferisci `.then` o `async/await`  
2. **Gestisci sempre gli errori** → con `.catch()` o `try/catch`  
3. **Chaining vs Async/Await** → usa async/await per sequenze leggibili  
4. **Non creare nuove Promise inutilmente** → se la funzione già ritorna una Promise, basta `return`  

---

## Piccola sintesi visiva

```text
Funzione → ritorna Promise
    ├─ resolve(valore) → then()
    ├─ reject(errore) → catch()
    └─ finally() → sempre eseguito
```

---

## Esempio completo “pronto all’uso”

```javascript
function fetchUserData(id) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (id > 0) {
                resolve({ id, nome: "Lorenzo" });
            } else {
                reject("ID non valido");
            }
        }, 1500);
    });
}

async function main() {
    try {
        const user = await fetchUserData(1);
        console.log("Utente:", user);
    } catch (err) {
        console.error(err);
    } finally {
        console.log("Fine esecuzione");
    }
}

main();
```

💡 **Nota**: salva questo file come `README.md` nel tuo progetto, così hai una vera e propria bibbia delle Promise sempre pronta da consultare.
