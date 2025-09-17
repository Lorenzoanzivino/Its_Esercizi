// Esercizio 3: Renderizzare Liste con .map()
// Obiettivo: Visualizzare dinamicamente una lista di elementi partendo da un array.
// Componente da creare: MenuRistorante.js
// Istruzioni:
// 1.​ Crea un file piatti.js in src ed esporta un array di oggetti. Ogni oggetto deve
// avere id, nome e prezzo.
// 2.​ Crea il componente MenuRistorante.js e importa l'array di piatti.
// 3.​ Usa il metodo .map() sull'array per renderizzare una lista <ul> di piatti.
// 4.​ Ogni <li> deve contenere il nome e il prezzo del piatto e deve avere un attributo
// key univoco (usa piatto.id).
// 5.​ Importa e usa <MenuRistorante /> in App.js.

import React from 'react'
import piatti from './piatti'

const MenuRistorante = () => {
    return (
        <div
            style={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center', // centra orizzontalmente
                padding: '20px',
                backgroundColor: '#f8f8f8',
                minHeight: '55vh',
                height: '20vh',                
                gap: '15px',
            }}
        >
            {piatti.map(piatto => (
                <div
                    key={piatto.id}
                    style={{
                        width: '300px',
                        padding: '15px',
                        border: '1px solid #ccc',
                        borderRadius: '8px',
                        boxShadow: '0 2px 6px rgba(0,0,0,0.1)',
                        backgroundColor: '#fff',
                        textAlign: 'center'
                    }}
                >
                    <h3 style={{margin: '0 0 10px 0'}}>{piatto.nome}</h3>
                    <h6 style={{margin: 0, fontWeight: 'bold'}}>{piatto.prezzo} €</h6>
                </div>
            ))}
        </div>
    )
}

export default MenuRistorante;