import React from 'react';

const Componente_Stampanumeri = () => {
  const numeri = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

return(
  numeri.map((numero) => {
    return <span key={numero}>{numero} -</span>
  })
)
}

export default Componente_Stampanumeri;