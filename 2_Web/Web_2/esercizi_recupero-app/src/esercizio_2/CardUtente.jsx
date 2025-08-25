import React from 'react';

function CardUtente(props) {
  return (
    <div style={{border: '1px solid gray', padding: '10px', margin: '10px', width: '200px'}}>
      <img src={props.imgUrl} alt="Avatar utente" style={{width: '100%'}} />
      <h2>{props.nome}</h2>
      <p>{props.email}</p>
    </div>
  );
}

export default CardUtente;