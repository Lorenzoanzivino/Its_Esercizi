import React, { useState } from 'react'

const PostForm = ({ aggiungiPost }) => {

    const [formData, setFormData] = useState({
        titolo: '',
        contenuto: ''
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({
            ...prev,
            [name]: value
        }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        aggiungiPost(formData);
        setFormData({ titolo: '', contenuto: '' });
    };

    return (
        <div
            style={{
                width: '100%',
                maxWidth: '400px',
                marginBottom: '30px',
            }}
        >
            <form onSubmit={handleSubmit}
                style={{
                    display: 'flex',
                    flexDirection: 'column',
                    gap: '10px',
                    padding: '20px',
                    border: '1px solid #ccc',
                    borderRadius: '8px',
                    backgroundColor: '#f9f9f9',
                }}
            >
                <div>
                    <label>Titolo:</label>
                    <input
                        type="text"
                        name="titolo"
                        value={formData.titolo}
                        onChange={handleChange}
                        style={{
                            padding: '8px',
                            fontSize: '16px',
                        }}
                    />
                </div>
                <div>
                    <label>Contenuto:</label>
                    <textarea
                        name="contenuto"
                        value={formData.contenuto}
                        onChange={handleChange}
                        style={{
                            padding: '8px',
                            fontSize: '16px',
                            height: '80px'
                        }}
                    />
                </div>
                <button type="submit">Submit</button>
            </form>
        </div>
    )
}

export default PostForm