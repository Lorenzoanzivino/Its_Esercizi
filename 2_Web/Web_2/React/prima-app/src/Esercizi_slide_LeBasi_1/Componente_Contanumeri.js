import React from 'react'

const Componente_Contanumeri = () => {
  const numeri = [];
  for (let i = 0; i <= 20; i += 2) {
    numeri.push(i);
  }

  return (
    <div>
      {numeri.map(i => (
        <span key={i}>
          {i} -
        </span>
      ))}
    </div>
  );
}

export default Componente_Contanumeri;
