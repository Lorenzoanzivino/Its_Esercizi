import React, { useState } from "react";

const UserCrud = () => {
    const [persona, setPersona] = useState({
        id: "",
        nome: "",
        cognome: "",
        email: "",
        telefono: "",
    });

    const [persone, setPersone] = useState([]);

    const gestioneDati = (e) => {
        e.preventDefault();
        if (persona.nome && persona.cognome && persona.id && persona.email && persona.telefono) {
            setPersone([...persone, { ...persona }]);
            setPersona({
                id: "",
                nome: "",
                cognome: "",
                email: "",
                telefono: "",
            });
        } else {
            alert("Compila tutti i campi");
        }
    };

    const handler = (e) => {
        const { name, value } = e.target;
        setPersona({ ...persona, [name]: value });
    };

    const eliminaUtente = (id) => {
        const nuovaLista = persone.filter((p) => p.id !== id);
        setPersone(nuovaLista);
    };

    return (
        <div className="container border py-3">
            <form className="row g-3" onSubmit={gestioneDati}>
                <div className="col-md-6">
                    <label htmlFor="inputNome" className="form-label">
                        Nome
                    </label>
                    <input
                        type="text"
                        className="form-control"
                        id="inputNome"
                        name="nome"
                        value={persona.nome}
                        onChange={handler}
                    />
                </div>
                <div className="col-md-6">
                    <label htmlFor="inputCognome" className="form-label">
                        Cognome
                    </label>
                    <input
                        type="text"
                        className="form-control"
                        id="inputCognome"
                        name="cognome"
                        value={persona.cognome}
                        onChange={handler}
                    />
                </div>

                <div className="col-md-6">
                    <label htmlFor="inputId" className="form-label">
                        ID
                    </label>
                    <input
                        type="text"
                        className="form-control"
                        id="inputId"
                        name="id"
                        value={persona.id}
                        onChange={handler}
                    />
                </div>

                <div className="col-md-6">
                    <label htmlFor="inputTelefono" className="form-label">
                        Telefono
                    </label>
                    <input
                        type="text"
                        className="form-control"
                        id="inputTelefono"
                        name="telefono"
                        value={persona.telefono}
                        onChange={handler}
                    />
                </div>

                <div className="col-12">
                    <label htmlFor="inputEmail" className="form-label">
                        Email
                    </label>
                    <input
                        type="text"
                        className="form-control"
                        id="inputEmail"
                        name="email"
                        value={persona.email}
                        onChange={handler}
                    />
                </div>

                <div className="col-12">
                    <button type="submit" className="btn btn-primary">
                        Invia
                    </button>
                </div>
            </form>

            <hr />

            <h4>Lista Utenti</h4>
            {persone.length === 0 ? (
                <p>Nessun utente inserito.</p>
            ) : (
                <ul className="list-group mt-3">
                    {persone.map((p, index) => (
                        <li key={index} className="list-group-item d-flex justify-content-between align-items-center">
                            <div>
                                <strong>ID:</strong> {p.id} | <strong>Nome:</strong> {p.nome} | <strong>Cognome:</strong> {p.cognome} | <strong>Email:</strong> {p.email} | <strong>Telefono:</strong> {p.telefono}
                            </div>
                            <button className="btn btn-danger btn-sm" onClick={() => eliminaUtente(p.id)}>
                                Elimina
                            </button>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default UserCrud;
