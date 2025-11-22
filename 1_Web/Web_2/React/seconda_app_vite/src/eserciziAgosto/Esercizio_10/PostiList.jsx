import React from 'react'

const PostList = (props) => {
    return (
        <div
            style={{
                width: '100%',
                maxWidth: '600px',
                display: 'flex',
                flexDirection: 'column',
                gap: '15px',
            }}
        >
            {props.posts.map((post, index) => (
                <div key={index} style={{
                    padding: '15px',
                    border: '1px solid #ddd',
                    borderRadius: '6px',
                    backgroundColor: '#fff',
                    boxShadow: '0 2px 4px rgba(0,0,0,0.05)',
                }}>
                    <h2>{post.titolo}</h2>
                    <p>{post.contenuto}</p>
                </div>
            ))}
        </div>
    );
}

export default PostList