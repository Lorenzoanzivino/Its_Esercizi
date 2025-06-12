import './App.css';
import Componente1 from './componente1';

function App() {
  let nome = "Lorenzo"
  return (
    <div className="App">
      <Componente1></Componente1>
      <h1>Prima App React : {nome}</h1>
      <h2>
        {
          new Date().toLocaleDateString()+" "+ new Date().toLocaleTimeString()
        }
      </h2>
    </div>
  );
}

export default App;
