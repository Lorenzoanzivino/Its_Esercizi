import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';


const Persona = ({nome, cognome, eta}) => {
    //const {nome, cognome, eta} = props; // Destrutturazione 
  
    return(
      <div className="border p-3 m-3 text-center">
        <h3>{nome} {cognome}</h3>
        <h5>Età: {eta}</h5>
      </div>
    );
  };
  
export default Persona;