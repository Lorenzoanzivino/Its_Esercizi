import React from 'react'
/*
5- Creare un componente Biblioteca che visualizza una lista di libri e permette agli
utenti di aggiungere un nuovo libro alla lista.
Componente Biblioteca: Il componente principale che ospita gli altri componenti.
Componente BookList: Un componente che mostra la lista dei libri.
Componente AddBookForm: Un componente che al momento mostra solo la scritta ‘form
inserimento libro’ con un pulsante che al click mostra un alert(‘libro inserito’)
Simulazione di Aggiornamento: Utilizzare una funzione per aggiungere un libro alla lista.
Nota Bene: al momento non ci sarà il render lato front end ma andremo a stampare tutto in
console
*/

function libro(nome, autore, id){
  this.id = id
  this.nome = nome
  this.autore = autore
}

let libri = [new libro("Divina Commedia", "Dante Alighieri", "DADIVCOMM"), new libro("Libro", "Qualcuno", "AAAA")]

function add_book(nome, autore, id){
  alert("libro inserito")
  libri.push(new libro(nome, autore, id))
  console.log(libri)
}

const BookList = () => {
  return (
    <ul>{libri.map((book) => {
      return <li key={book.id}>{book.nome} - {book.autore}</li>
    })}</ul>
  )
}

const AddBookForm = () => {
  return (
    <>
      <input type='text' id="nome"></input>
      <button onClick={() => add_book(document.getElementById("nome").value)}> form inserimento libro</button>
    </>
  )
}

export const Biblioteca = () => {
  return (
    <>
      <BookList />
      <AddBookForm></AddBookForm>
    </>
  )
}

export default Biblioteca