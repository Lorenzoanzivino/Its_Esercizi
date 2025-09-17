import './App.css'
import Saluto from './eserciziAgosto/Esercizio_01/Saluto'
import CardUtente from './eserciziAgosto/Esercizio_02/CardUtente'
import MenuRistorante from './eserciziAgosto/Esercizio_03/MenuRistorante'
import Termostato from './eserciziAgosto/Esercizio_04/Termostato'
import CampoRicerca from './eserciziAgosto/Esercizio_05/CampoRicerca'
import MessaggioSegreto from './eserciziAgosto/Esercizio_06/messaggioSegreto'
import AggiornaTitolo from './eserciziAgosto/Esercizio_07/AggiornaTitolo'
import GalleriaFoto from './eserciziAgosto/Esercizio_08/GalleriaFoto'
import ModuloContatti from './eserciziAgosto/Esercizio_09/ModuloContatti'
import BlogApp from './eserciziAgosto/Esercizio_10/BlogApp'



function App() {
  /* Persona Singola */
  const persona = {
    nome: "ugo",
    email: "rob@rob.it",
    imgUrl: "https://placehold.co/600x400/png",
  }

  /* Lista di Persone */
  const persone = [
    {
      nome: "ugo",
      email: "rob@rob.it",
      imgUrl: "https://placehold.co/600x400/png",
    },
    {
      nome: "Pippo",
      email: "rob@rob.it",
      imgUrl: "https://placehold.co/600x400/png",
    },
    {
      nome: "Gino",
      email: "rob@rob.it",
      imgUrl: "https://placehold.co/600x400/png",
    },
  ];

  return (
    <>
      <>Esercizio 01</>
      <Saluto></Saluto>
      <>Esercizio 02</>
      {/*<CardUtente
        nome="Roberto"
        email="rob@rob.it"
        imgUrl="https://placehold.co/600x400/png"
      ></CardUtente>

      <CardUtente {...persona}></CardUtente>*/}

      <div className="row">
        {persone.map((p) => {
          return (
            <div className="col">
              <CardUtente {...p}></CardUtente>
            </div>
          );
        })}
      </div>
      <>Esercizio 03</>
      <MenuRistorante></MenuRistorante>
      <>Esercizio 04</>
      <Termostato></Termostato>
      <>Esercizio 05</>
      <CampoRicerca></CampoRicerca>
      <>Esercizio 06</>
      <MessaggioSegreto></MessaggioSegreto>
      <>Esercizio 07</>
      <AggiornaTitolo></AggiornaTitolo>
      <>Esercizio 08</>
      <GalleriaFoto></GalleriaFoto>
      <>Esercizio 09</>
      <ModuloContatti />
      <>Esercizio 10</>
      <BlogApp></BlogApp>
    </>
  )
}

export default App