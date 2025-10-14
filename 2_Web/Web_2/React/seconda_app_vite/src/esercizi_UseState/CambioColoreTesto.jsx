import React, { useState } from 'react';

const CambioColoreTesto = () => {
  const [colore, setColore] = useState("black")
  return (
    <div className="text-center">
      <button onClick={() => setColore("red")}>Rosso</button>
      <button onClick={() => setColore("green")}>Verde</button>
      <button onClick={() => setColore("blue")}>Blu</button>
      <h1 style={{ color: colore }}>Cambia il colore del testo</h1>
    </div>
  );
}
export default CambioColoreTesto;