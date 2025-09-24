import './App.css'
import { useState } from 'react'
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
import Navbar from './eserciziAgosto/NavBar'
import TodoApp from './eserciziAgosto/Esercizio_11/TodoApp'

function App() {
  const [esercizio, setEsercizio] = useState('')

  const renderCondzionale = () => {
    switch (esercizio) {
      case 'Saluto':
        return <Saluto />

      case 'CardUtente':
        return <CardUtente />

      case 'MenuRistorante':
        return <MenuRistorante />

      case 'Termostato':
        return <Termostato />

      case 'CampoRicerca':
        return <CampoRicerca />

      case 'MessaggioSegreto':
        return <MessaggioSegreto />

      case 'AggiornaTitolo':
        return <AggiornaTitolo />

      case 'GalleriaFoto':
        return <GalleriaFoto />

      case 'ModuloContatti':
        return <ModuloContatti />

      case 'BlogApp':
        return <BlogApp />

      case 'TodoApp':
        return <TodoApp />
    }

  };
  return (
    <>
      <Navbar onSetEsercizio={setEsercizio} />
      <div>{renderCondzionale()}</div>
    </>
  )
}

export default App;