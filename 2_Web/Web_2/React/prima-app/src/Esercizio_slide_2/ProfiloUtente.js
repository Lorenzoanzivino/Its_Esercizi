import React from "react";

const ProfiloUtente = ({ utente }) => {
  const mostraDettagli = () => {
    alert(
      `ID: ${utente.id}\nNome: ${utente.nome} ${utente.cognome}\nEtà: ${utente.eta}\nProfessione: ${utente.professione}\nEmail: ${utente.email}`
    );
  };

  return (
    <div className="card h-100" onClick={mostraDettagli}>
      <div className="card-header text-center">
        <h5>{utente.nome} {utente.cognome}</h5>
      </div>
      <div className="card-body text-center">
        <span className="badge bg-primary mb-2">Età: {utente.eta}</span>
        <p className="mb-1">{utente.professione}</p>
        <p className="mb-0">{utente.email}</p>
      </div>
      <div className="card-footer text-center">
        <small className="text-muted">Clicca per dettagli</small>
      </div>
    </div>
  );
};

export default ProfiloUtente;
