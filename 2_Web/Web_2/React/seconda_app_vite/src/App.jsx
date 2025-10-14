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
import TodoApp from './eserciziAgosto/todoList/TodoApp'
import MainComponent from './eserciziAgosto/MainComponent'
import ProvaRoutes from './routes/ProvaRoutes'
import MostraNascondi from './esercizi_UseState/MostraNascondi'
import CambioColoreTesto from './esercizi_UseState/CambioColoreTesto'
import EchoInput from './esercizi_UseState/EchoInput'
import SelettorePizza from './esercizi_UseState/SelettorePizza'
import SkillsSelector from './CheckboxMultipleCounter/SkillsSelector'

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

      case 'MainComponent':
        return <MainComponent />
    }

  };
  return (
    <>
      <Navbar onSetEsercizio={setEsercizio} />
      <div>{renderCondzionale()}</div>
      <br/><br/>
      <ProvaRoutes></ProvaRoutes>
      <br/><br/>
      <h3 className="text-center">Esercizio Mostra/Nascondi</h3>
      <MostraNascondi></MostraNascondi>
      <br/><br/>
      <h3 className="text-center">Esercizio Cambia colore testo</h3>
      <CambioColoreTesto></CambioColoreTesto>
      <br/><br/>
      <h3 className="text-center">Esercizio Echo Testo</h3>
      <EchoInput></EchoInput>
      <br/><br/>
      <h3 className="text-center">Esercizio Selettore Pizza</h3>
      <SelettorePizza></SelettorePizza>
      <br/><br/>
      <h3 className="text-center">Esercizio SkillsSelector</h3>
      <SkillsSelector></SkillsSelector>
      <br/><br/>
    </>
  );
};

export default App;