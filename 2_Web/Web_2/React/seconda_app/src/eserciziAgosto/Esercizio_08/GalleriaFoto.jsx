// Esercizio 8: Caricare Dati da un Server (Data Fetching)Obiettivo: Usare useEffect per caricare dati da un'API esterna e gestire gli stati di
// caricamento ed errore. Componente da creare: GalleriaFoto.js
// Istruzioni:
// 1.​ Crea il componente GalleriaFoto.js.
// 2.​ Definisci tre stati: foto (array vuoto), staCaricando (true), errore (null).
// 3.​ Usa useEffect (con dipendenza []) per fare una fetch all'URL:
// https://jsonplaceholder.typicode.com/photos?_limit=10.
// 4.​ Dentro useEffect, usa una funzione async/await e un blocco try/catch.
// 5.​ Nel try, se la richiesta va a buon fine, popola lo stato foto e imposta
// staCaricando a false.
// 6.​ Nel catch, imposta lo stato errore con il messaggio di errore e staCaricando a
// false.
// 7.​ Nel JSX, gestisci i tre stati: mostra un messaggio di caricamento, un messaggio di
// errore, o la galleria di foto (mappando l'array foto e mostrando le immagini).


import React, { useEffect, useState } from 'react';
import axios from 'axios';

const url = 'https://jsonplaceholder.typicode.com/photos?_limit=10';

const GalleriaFoto = () => {

    const [foto, setFoto] = useState([]);
    const [isLoading, setIsLoading] = useState(true);
    const [isError, setIsError] = useState(null);

    const getData = async () => {
        setIsError(false);
        setIsLoading(true);
        try {
            const response = await axios.get(url);
            setFoto(response.data);
        } catch (err) {
            console.log(err)
            setIsError(true);
        }
        setIsLoading(false);
    };

    useEffect(() => {
        getData();
    }, [])

    if (isLoading) {
        return <h3>Caricamento...</h3>
    };

    if (isError) {
        return <h3>Si è verificato un'errore</h3>
    };

    return (
        <ul>
            {
                foto.map((f) => {
                    return (
                        <li key={f.id}>
                            <div>
                                <img src={f.url} alt="" />
                                <h5>{f.title}</h5>
                            </div>
                        </li>
                    )
                })
            }
        </ul>
    )
}

export default GalleriaFoto