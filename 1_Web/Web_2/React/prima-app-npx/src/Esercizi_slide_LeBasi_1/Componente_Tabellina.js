import React from 'react';

const Componente_Tabellina = () => {
  const numero = 5;
  const valori = [];

  // Popolo un array con i numeri da 1 a 10
  for (let i = 1; i <= 10; i++) {
    valori.push(i);
  }

  return (
    <div>
      <p>Tabellina del {numero}</p>
      {valori.map(i => (
        <div key={i}>
          {numero} x {i} = {numero * i}
        </div>
      ))}
    </div>
  );
};

export default Componente_Tabellina;
