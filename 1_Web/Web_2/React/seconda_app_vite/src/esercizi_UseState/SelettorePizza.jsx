import React, { useState } from 'react';

const SelettorePizza = () => {
    const [scelta, setScelta] = useState({nome: "", count: 0});

    const selezionaPizza = (nomePizza) => {
    setScelta(prev => {
        if (prev.nome === nomePizza) {
            return { nome: nomePizza, count: prev.count + 1 }
        } else {
            return { nome: nomePizza, count: 1 }
        }
    });
};

  return (
    <div className="text-center">
        <button onClick={() => selezionaPizza("Margherita")}>Margherita</button>
        <button onClick={() => selezionaPizza("Diavola")}>Diavola</button>
        <button onClick={() => selezionaPizza("Capricciosa")}>Capricciosa</button>
        <button onClick={() => selezionaPizza("Marinara")}>Marinara</button>
        <p>Hai scelto la pizza : {scelta.nome} {scelta.count > 1 ? `x${scelta.count}` : ""}</p>
        
    </div>
  );
}
export default SelettorePizza;