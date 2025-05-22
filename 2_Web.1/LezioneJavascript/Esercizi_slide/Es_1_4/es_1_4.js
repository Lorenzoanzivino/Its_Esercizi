let valore = '50';

console.log("Valore iniziale:", valore);
console.log("Tipo:", typeof valore);

// Verifica se è numerico
let isNumeric = !isNaN(valore);
console.log("È numerico?", isNumeric);

// Conversione a numero
valore = Number(valore);

console.log("Valore dopo conversione:", valore);
console.log("Tipo dopo conversione:", typeof valore);
