// Giorni della settimana come stringa separata da virgole
let giorni = "Lunedì,Martedì,Mercoledì,Giovedì,Venerdì,Sabato,Domenica";

// Stampare tutto in una riga con virgole
console.log("Giorni separati da virgola:");
console.log(giorni);

// Con una sola modifica: stampa uno sotto l'altro
console.log("\nGiorni uno sotto l'altro:");
console.log(giorni.split(",").join("\n"));
