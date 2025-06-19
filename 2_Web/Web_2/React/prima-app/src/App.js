import './App.css';
import Clock from './Clock';
import Componente1 from './Componente1';
import Persona from './Esercizi_slide_LeBasi_1/Componente_Persona';
import Componente_Tabellina from './Esercizi_slide_LeBasi_1/Componente_Tabellina'; 
import Componente_Stampanumeri from './Esercizi_slide_LeBasi_1/Componente_Stampanumeri';
import Componente_Contanumeri from './Esercizi_slide_LeBasi_1/Componente_Contanumeri';

import Biblioteca from './Esercizi_slide_LeBasi_1/Componente_Biblioteca';;


function App() {
  let nome = "Lorenzo"
  return (
    <div className="App">
      <br/>
      <Componente1></Componente1>
      <Componente1></Componente1>
      <br/>
      <h5>{ "-".repeat(100) }</h5> {/* Stampa 100 Trattini "-" */}
      <h1>Prima App React: {nome}</h1>
      <br/>
      <h5>{ "-".repeat(100) }</h5> {/* Stampa 100 Trattini "-" */}
      <h2>
        {
        new Date().toLocaleDateString()+" - "+ new Date().toLocaleTimeString()
        }
      </h2>
      <Clock timezone="0" country="Italia"></Clock>
      <Clock timezone="-6" country="USA"></Clock>
      <Clock timezone="7" country="Japan"></Clock>
      <br/>
      <h5>{ "-".repeat(100) }</h5> {/* Stampa 100 Trattini "-" */}
      <Persona nome="Marco" cognome="Verdi" eta={28} />
      <br/>
      <h5>{ "-".repeat(100) }</h5> {/* Stampa 100 Trattini "-" */}
      <p><Componente_Tabellina/></p>
      <br/>
      <h5>{ "-".repeat(100) }</h5> {/* Stampa 100 Trattini "-" */}
      <div>Numeri da 1/10 : </div>
      <span><Componente_Stampanumeri/></span>
      <br/>
      <h5>{ "-".repeat(100) }</h5> {/* Stampa 100 Trattini "-" */}
      <div>Numeri da 0/20 : </div>
      <span><Componente_Contanumeri/></span>
      <br/>
      <h5>{ "-".repeat(100) }</h5> {/* Stampa 100 Trattini "-" */}
      <h2>La mia Biblioteca</h2>
      <Biblioteca 
        libro1="Il nome della rosa" 
        libro2="1984" 
        libro3="Harry Potter" 
      />
    </div>
  );
}

export default App;

// FRAGMENT 
// <></> oppure <React.Fragment></React.Fragment> 
// servono per racchiudere più div fratelli con un tag che non viene renderizzato