import React, { useState } from 'react';

const MostraNascondi = () => {
  const [mostra, setMostra] = useState(true);

  const toggleMostra = () => {
    setMostra(!mostra);
  };

  // Variabile per il testo del bottone
  let testoBottone;
  if (mostra) {
    testoBottone = 'Nascondi testo';
  } else {
    testoBottone = 'Mostra testo';
  }

  // Variabile per il paragrafo da mostrare/nascondere
  let paragrafo;
  if (mostra) {
    paragrafo = <p>Questo è il testo che puoi mostrare o nascondere cliccando il bottone.</p>;
  }

  // Variabile per lo stato attuale
  let statoAttuale;
  if (mostra) {
    statoAttuale = 'VISIBILE';
  } else {
    statoAttuale = 'NASCOSTO';
  }

  return (
    <div className="text-center">
      <button onClick={toggleMostra}>{testoBottone}</button>
      {paragrafo}
      <p>Stato attuale: <strong>{statoAttuale}</strong></p>
    </div>
  );
};

export default MostraNascondi;
