import React from 'react';
import Saluto from './esercizio_1/Saluto';
import CardUtente from './esercizio_2/CardUtente';

function App() {
  return (
    <div>
      <Saluto />

      {/* Richiamo CardUtente due volte con dati diversi */}
      <CardUtente
        nome="Lorenzo Anzivino"
        email="lorenzo@example.com"
        imgUrl="https://placehold.co/200x200"
      />
      <CardUtente
        nome="Maria Rossi"
        email="maria@example.com"
        imgUrl="https://placehold.co/200x200"
      />
    </div>
  );
}

export default App;