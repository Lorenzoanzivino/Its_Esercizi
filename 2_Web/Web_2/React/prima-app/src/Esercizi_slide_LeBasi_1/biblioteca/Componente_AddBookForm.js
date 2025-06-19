import React from "react";

function AddBookForm({ onAdd }) {
  const handleClick = () => {
    alert("libro inserito");
    onAdd("Nuovo Libro");
  };

  return (
    <div>
      <p>form inserimento libro</p>
      <button onClick={handleClick}>Aggiungi Libro</button>
    </div>
  );
}

export default AddBookForm;