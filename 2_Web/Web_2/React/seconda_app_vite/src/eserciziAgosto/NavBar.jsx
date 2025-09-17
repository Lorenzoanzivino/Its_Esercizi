import React, { useState } from 'react'

const Navbar = ({onSetEsercizio}) => {
    const lista_esercizi = ["Saluto", "CardUtente", "MenuRistorante", "Termostato", "CampoRicerca", "MessaggioSegreto", "AggiornaTitolo", "GalleriaFoto", "ModuloContatti", "BlogApp", "TodoApp"]

    return (
        <div>
            <nav className="navbar navbar-expand-lg bg-body-tertiary">
                <div className="container-fluid">
                    <a className="navbar-brand" href="#">
                        Esercizi
                    </a>
                    <button
                        className="navbar-toggler"
                        type="button"
                        data-bs-toggle="collapse"
                        data-bs-target="#navbarText"
                        aria-controls="navbarText"
                        aria-expanded="false"
                        aria-label="Toggle navigation"
                    >
                        <span className="navbar-toggler-icon" />
                    </button>
                    <div className="collapse navbar-collapse" id="navbarText">
                        <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                            {lista_esercizi.map((item) => (
                                <li className="nav-item">
                                    <button onClick={() => { onSetEsercizio(item) }}>{item}</button>
                                </li>))}
                        </ul>
                    </div>
                </div>
            </nav>
        </div>
    )
}

export default Navbar;