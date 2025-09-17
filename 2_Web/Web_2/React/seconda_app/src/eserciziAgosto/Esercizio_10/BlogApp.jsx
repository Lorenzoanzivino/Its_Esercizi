// Esercizio 10: Mini-Blog - Unire Tutti i Concetti
// Obiettivo: Creare una piccola applicazione che combina gestione dello stato, liste, form e
// componenti. Componenti da creare: BlogApp.js, PostForm.js, PostList.js
// Istruzioni:
// 1. BlogApp.js (Genitore):
// ○ Qui vivrà lo stato principale: const [posts, setPosts] =
// useState([]);.
// ○ Crea una funzione aggiungiPost che riceve un oggetto post e lo aggiunge
// all'array posts.
// ○ Renderizza <PostForm /> e <PostList />, passando le funzioni e i dati
// necessari come props.
// 2. PostForm.js (Figlio):
// ○ Riceve aggiungiPost come prop.
// ○ Contiene un form con input per titolo e contenuto.
// ○ Alla sottomissione del form, chiama aggiungiPost con i dati del nuovo
// post.
// 3. PostList.js (Figlio):
// ○ Riceve posts come prop.
// ○ Mappa l'array posts e visualizza ogni post (titolo e contenuto) in un
// componente div o article dedicato.


import React, { useState } from 'react';
import PostForm from './PostForm';
import PostList from './PostList';

const BlogApp = () => {

    const [posts, setPosts] = useState([]);

    const aggiungiPost = (nuovoPost) => {
        setPosts([...posts, nuovoPost]);
    };

    return (
        <div
            style={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                fontFamily: 'Arial, sans-serif',
                padding: '20px',
            }}
        >
            <PostForm aggiungiPost={aggiungiPost} />
            <PostList posts={posts} />
        </div>
    )
}

export default BlogApp