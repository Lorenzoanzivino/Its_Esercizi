import React, { useState } from 'react';

const UserCrud = () => {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    id: '',
    phone: '',
    email: '',
    password: '',
    check: false,
  });

  const [users, setUsers] = useState([]);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Controlla che firstName e lastName siano compilati
    if (!formData.firstName || !formData.lastName) {
      alert("Compila almeno nome e cognome");
      return;
    }

    // Aggiunge il nuovo utente alla lista
    setUsers((prevUsers) => [...prevUsers, formData]);

    // Reset del form
    setFormData({
      firstName: '',
      lastName: '',
      id: '',
      phone: '',
      email: '',
      password: '',
      check: false,
    });
  };

  return (
    <div className="container mt-4 border py-3">
      {/* --- FORM --- */}
      <form onSubmit={handleSubmit}>
        <div className="row mb-3">
          <div className="col-md-6">
            <label htmlFor="firstName" className="form-label">First name</label>
            <input
              type="text"
              className="form-control"
              id="firstName"
              placeholder="First name"
              name="firstName"
              value={formData.firstName}
              onChange={handleChange}
            />
          </div>
          <div className="col-md-6">
            <label htmlFor="lastName" className="form-label">Last name</label>
            <input
              type="text"
              className="form-control"
              id="lastName"
              placeholder="Last name"
              name="lastName"
              value={formData.lastName}
              onChange={handleChange}
            />
          </div>
        </div>

        <div className="mb-3">
          <label htmlFor="userId" className="form-label">ID</label>
          <input
            type="text"
            className="form-control"
            id="userId"
            name="id"
            placeholder="Enter your ID"
            value={formData.id}
            onChange={handleChange}
          />
        </div>

        <div className="mb-3">
          <label htmlFor="phone" className="form-label">Numero di Telefono</label>
          <input
            type="tel"
            className="form-control"
            id="phone"
            name="phone"
            placeholder="Es. +39 123 4567890"
            pattern="^\+?[0-9\s\-]{7,15}$"
            value={formData.phone}
            onChange={handleChange}
          />
        </div>

        <div className="mb-3">
          <label htmlFor="email" className="form-label">Email address</label>
          <input
            type="email"
            className="form-control"
            id="email"
            name="email"
            placeholder="Enter email"
            value={formData.email}
            onChange={handleChange}
          />
          <small className="form-text text-muted">
            We'll never share your email with anyone else.
          </small>
        </div>

        <div className="mb-3">
          <label htmlFor="password" className="form-label">Password</label>
          <input
            type="password"
            className="form-control"
            id="password"
            name="password"
            placeholder="Password"
            value={formData.password}
            onChange={handleChange}
          />
        </div>

        <div className="form-check mb-3">
          <input
            type="checkbox"
            className="form-check-input"
            id="check"
            name="check"
            checked={formData.check}
            onChange={handleChange}
          />
          <label className="form-check-label" htmlFor="check">
            Check me out
          </label>
        </div>

        <button type="submit" className="btn btn-primary">Submit</button>
      </form>

      {/* --- LISTA UTENTI --- */}
      <div className="mt-5">
        <h4>Lista Utenti</h4>
        {users.length === 0 ? (
          <p>Nessun utente inserito.</p>
        ) : (
          <ul className="list-group">
            {users.map((user, index) => (
              <li key={index} className="list-group-item">
                <strong>{user.firstName} {user.lastName}</strong> - ID: {user.id} - 📞 {user.phone} - 📧 {user.email}
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
};

export default UserCrud;
