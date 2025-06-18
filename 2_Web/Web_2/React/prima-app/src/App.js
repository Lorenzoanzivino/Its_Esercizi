import './App.css';
import Clock from './Clock';
import Componente1 from './Componente1';

function App() {
  let nome = "Lorenzo"
  return (
    <div className="App">
      <br/>
      <Componente1></Componente1>
      <Componente1></Componente1>
      <Componente1></Componente1>
      <Componente1/>
      <br/>
      <h1>Prima App React: {nome}</h1>
      <br/>
      <h2>
        {
        new Date().toLocaleDateString()+" - "+ new Date().toLocaleTimeString()
        }
      </h2>
      <Clock timezone="0" country="Italia"></Clock>
      <Clock timezone="-6" country="USA"></Clock>
      <Clock timezone="7" country="Japan"></Clock>
    </div>
  );
}

export default App;

// FRAGMENT 
// <></> oppure <React.Fragment></React.Fragment> 
// servono per racchiudere più div fratelli con un tag che non viene renderizzato