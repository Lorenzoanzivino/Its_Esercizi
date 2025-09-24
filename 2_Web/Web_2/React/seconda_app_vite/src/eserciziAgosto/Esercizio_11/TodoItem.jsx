// 4. TodoItem.js (Nipote):
// ○ Riceve il singolo oggetto task e le funzioni handleDeleteTask e
// handleToggleTask come props.
// ○ Visualizza il testo del task. Applica uno stile per sbarrare il testo se
// task.completed è true.
// ○ Aggiungi un checkbox che, al onChange, chiami handleToggleTask con
// l'id e lo stato completed invertito.
// ○ Aggiungi un bottone "Elimina" che, al onClick, chiami handleDeleteTask
// con l'id del task.


import React from 'react'

const TodoItem = ({task, onDeleteTask, onToggleTask}) => {
  return (
    <li className="list-group-item d-flex justify-content-between">
      <input 
        type="checkbox"
        className="form-check-input me-2"
        checked={task.completed}
        onChange={() => onToggleTask(task.id, task.completed)}
      ></input>
      <span
        style={{textDecoration: task.completed ? "line-through" : "none"}}
      >{task.text}</span>
      <button class="btn btn-danger" onClick={() => onDeleteTask(task.id)}>DELETE</button>
    </li>
  )
}

export default TodoItem