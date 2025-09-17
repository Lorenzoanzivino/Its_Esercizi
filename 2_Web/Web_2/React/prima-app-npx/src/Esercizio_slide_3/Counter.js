import React from 'react'
import { useState } from 'react';

function Counter() {
    const [contatore, setContatore] = useState(0);

    const aumenta = () => {
        setContatore(contatore + 1);
    };

    const diminuisci = () => {
        setContatore(contatore - 1);
    };

    return (
        <div className="container d-flex flex-column align-items-center justify-content-center" style={{ minHeight: '200px' }}>
            <h1 className="mb-4">Contatore</h1>
            <div className="display-4 mb-4">{contatore}</div>
            <div className="btn-group">
                <button className="btn btn-success" onClick={aumenta}>
                    Aumenta
                </button>
                <button className="btn btn-danger" onClick={diminuisci}>
                    Diminuisci
                </button>
            </div>
        </div>
    );
}
export default Counter;

//<React.StrictMode>
    //<Counter></Counter>


  //</React.StrictMode>