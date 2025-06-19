import React, { useState } from "react";
import BookList from './Componente_Booklist';
import AddBookForm from './Componente_AddBookForm';

function Biblioteca() {
  const [libri, setLibri] = useState([
    "Il nome della rosa",
    "1984",
    "Harry Potter",
  ]);

  const aggiungiLibro = (nuovoLibro) => {
    setLibri((vecchiLibri) => [...vecchiLibri, nuovoLibro]);
  };

  return (
    <div>
      <h1>Biblioteca</h1>
      <BookList libri={libri} />
      <AddBookForm onAdd={aggiungiLibro} />
    </div>
  );
}

export default Biblioteca;
