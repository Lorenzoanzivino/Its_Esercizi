import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Clock from './Clock';
import Componente1 from './Componente1';
import Persona from './Esercizi_slide_LeBasi_1/Componente_Persona';
import Componente_Tabellina from './Esercizi_slide_LeBasi_1/Componente_Tabellina'; 
import Componente_Stampanumeri from './Esercizi_slide_LeBasi_1/Componente_Stampanumeri';
import Componente_Contanumeri from './Esercizi_slide_LeBasi_1/Componente_Contanumeri';
import Biblioteca from './Esercizi_slide_LeBasi_1/Componente_Biblioteca';
import ProfiloUtente from './Esercizio_slide_2/ProfiloUtente';
import Counter from './Esercizio_slide_3/Counter';
import Form from './Form';
import UserCrud from './Manage_user/UserCrud';

function App() {
  const nome = "Lorenzo";

  const utenti = [
    {
      id: 123456,
      nome: 'Stefano',
      cognome: 'Reali',
      eta: 34,
      professione: 'Sviluppatore Cloud',
      email: 'stefano.reali@mail.com',
    },
    {
      id: 151232,
      nome: 'Lorenzo',
      cognome: 'Anzivino',
      eta: 27,
      professione: 'Graphic Designer',
      email: 'lorenzo.anzivino@mail.com',
    },
    {
      id: 31235215,
      nome: 'Marcel',
      cognome: 'Movileanu',
      eta: 23,
      professione: 'Sviluppatore Cloud',
      email: 'marcel.movileanu@mail.com',
    },
    {
      id: 31233315,
      nome: 'Francesco',
      cognome: 'Magno',
      eta: 23,
      professione: 'Sviluppatore Cloud',
      email: 'francesco.magno@mail.com',
    }
  ];

  const orologi = [
    { timezone: 0, country: 'Italia', emoji: '🇮🇹' },
    { timezone: -6, country: 'USA', emoji: '🇺🇸' },
    { timezone: 7, country: 'Japan', emoji: '🇯🇵' },
  ];

  return (
    <div className="App container mt-4">
      {/* ================== COMPOSIZIONE INIZIALE ================== */}
      <Componente1 />
      <br />

      <h5>{ "-".repeat(100) }</h5>
      <h1>Prima App React: {nome}</h1>
      <br />
      <h2>
        {new Date().toLocaleDateString() + " - " + new Date().toLocaleTimeString()}
      </h2>

      {/* ================== OROLOGI ================== */}
      {orologi.map((o, i) => (
        <p key={i} style={{ display: 'inline-flex', alignItems: 'center', gap: '8px' }}>
          <span role="img" aria-label={`bandiera ${o.country}`}>{o.emoji}</span>
          <Clock timezone={o.timezone} country={o.country} />
        </p>
      ))}

      <br />
      <h5>{ "-".repeat(100) }</h5>

      {/* ================== PERSONA ================== */}
      <Persona nome="Marco" cognome="Verdi" eta={28} />

      <br />
      <h5>{ "-".repeat(100) }</h5>

      {/* ================== TABELLA ================== */}
      <Componente_Tabellina />

      <br />
      <h5>{ "-".repeat(100) }</h5>

      {/* ================== NUMERI DA 1 A 10 ================== */}
      <h6>Numeri da 1 a 10:</h6>
      <Componente_Stampanumeri />

      <br />
      <h5>{ "-".repeat(100) }</h5>

      {/* ================== NUMERI DA 0 A 20 ================== */}
      <h6>Numeri da 0 a 20:</h6>
      <Componente_Contanumeri />

      <br />
      <h5>{ "-".repeat(100) }</h5>

      {/* ================== BIBLIOTECA ================== */}
      <h2>La mia Biblioteca</h2>
      <Biblioteca 
        libro1="Il nome della rosa" 
        libro2="1984" 
        libro3="Harry Potter" 
      />

      <h5>{ "-".repeat(100) }</h5>

      {/* ================== PROFILI UTENTI ================== */}
      <h2 className="mt-5 mb-4">Profili Utenti</h2>
      <div className="row">
        {utenti.map((utente) => (
          <div className="col-md-4 mb-4" key={utente.id}>
            <ProfiloUtente utente={utente} />
          </div>
        ))}
      </div>

      <h5>{ "-".repeat(100) }</h5>

      {/* ================== CONTATORE ================== */}
      <Counter />

      {/* ================== FORM ================== */}
      <h5>{ "-".repeat(100) }</h5>
      <h2>Form</h2>
      <Form></Form>

      <></>
      {/* ================== USER FORM ================== */}
      <h5>{ "-".repeat(100) }</h5>
      <h2>UserForm</h2>
      <UserCrud></UserCrud>

    </div>
  );
}

export default App;
