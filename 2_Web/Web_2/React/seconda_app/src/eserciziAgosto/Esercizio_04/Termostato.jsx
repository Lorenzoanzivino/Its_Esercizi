// Esercizio 4: Introduzione allo Stato con useState
// Obiettivo: Rendere un componente interattivo usando l'hook useState. Componente da
// creare: Termostato.js
// Istruzioni:
// 1.​ Crea il componente Termostato.js.
// 2.​ Importa useState da React.
// 3.​ Inizializza uno stato per la temperatura: temperatura
// 4.​ Visualizza la temperatura in un <h1>.
// 5.​ Aggiungi due bottoni, "+" e "-", che al onClick aumentino o diminuiscano la
// temperatura di 1 grado, chiamando setTemperatura.
// 6.​ Importa e usa <Termostato /> in App.js.


import React, { useState } from 'react';

const Termostato = () => {
  const [temperatura, setTemperatura] = useState(0);

  const aumenta = () => {
    setTemperatura(temperatura + 1);
  };

  const diminuisci = () => {
    setTemperatura(temperatura - 1);
  };

  return (
    <div
      style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: '100vh',
        flexDirection: 'column',
        gap: '10px'
      }}
    >
      <h1>{temperatura}°C</h1>
      <button onClick={aumenta}>TEMP UP</button>
      <button onClick={diminuisci}>TEMP DOWN</button>
    </div>
  );
};

export default Termostato;