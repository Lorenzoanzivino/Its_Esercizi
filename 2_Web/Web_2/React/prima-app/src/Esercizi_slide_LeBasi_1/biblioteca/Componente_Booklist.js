import React from "react";

function BookList({ libri }) {
  return (
    <ul>
      {libri.map((libro, index) => (
        <li key={index}>{libro}</li>
      ))}
    </ul>
  );
}

export default BookList;