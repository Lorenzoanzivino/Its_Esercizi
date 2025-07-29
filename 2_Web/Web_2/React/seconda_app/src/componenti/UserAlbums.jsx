import { useState, useEffect } from 'react'
import React from 'react'
import axios from 'axios';



const users_url = 'https://jsonplaceholder.typicode.com/users';
const albums_url = 'https://jsonplaceholder.typicode.com/albums';
const photos_url = 'https://jsonplaceholder.typicode.com/photos';

const UserAlbums = () => {
    const [isLoading, setIsLoading] = useState(true);
    const [isError, setIsError] = useState(true);
    const [users, setusers] = useState([]);
    const [selectedUser, setSelectedUser] = useState();

    const [albumIsLoading, setAlbumIsLoading] = useState(true);
    const [AlbumsError, setAlbumsIsError] = useState(true);
    const [albums, setAlbums] = useState([]);
    const [selectedAlbum, setSelectedAlbum] = useState();

    const [PhotosIsLoading, PhotosSetIsLoading] = useState(true);
    const [PhotosError, PhotosSetError] = useState(true);
    const [photos, setPhotos] = useState([]);
    const [selectedPhoto, setSelectedPhotos] = useState();

    const getUsersData = async () => {
        setIsError(false);
        setIsLoading(true);
        try {
            const response = await axios.get(users_url);
            setusers(response.data);
        } catch (err) {
            console.log(err);
            setIsError(true);
        }
        setIsLoading(false);
    };

    const getAlbumsData = async () => {
        setAlbumsIsError(false);
        setAlbumIsLoading(true);
        try {
            const response = await axios.get(`${albums_url}?userId=${selectedUser}`);
            setAlbums(response.data);
        } catch (err) {
            console.log(err);
            setAlbumsIsError(true);
        }
        setAlbumIsLoading(false);
    };

    const getPhotosData = async () => {
        PhotosSetError(false);
        PhotosSetIsLoading(true);
        try {
            const response = await axios.get(`${photos_url}?albumId=${selectedAlbum}`);
            setPhotos(response.data);
        } catch (err) {
            console.log(err);
            PhotosSetError(true);
        }
        PhotosSetIsLoading(false);
    };

    useEffect(() => {
        getUsersData();
    }, []);

    useEffect(() => {
        getAlbumsData(selectedUser);
    }, [selectedUser]);

    useEffect(() => {
        getPhotosData(selectedAlbum);
    }, [selectedAlbum]);

    if (isLoading || albumIsLoading || PhotosIsLoading) {
        return <Loading />;
    }

    if (isError || AlbumsError || PhotosError) {
        return <h3 className="text-danger text-center mt-4">Si è verificato un'errore</h3>;
    }

    const handleUsersChange = (e) => {
        setSelectedUser(e.target.value);
    };

    const handleAlbumsChange = (e) => {
        setSelectedAlbum(e.target.value);
    };

    return (
        <div className="container mt-5">
            <div className="row mb-4">
                <div className="col-md-6">
                    <label className="form-label">Utente</label>
                    <select
                        className="form-select"
                        value={selectedUser}
                        onChange={handleUsersChange}
                    >
                        <option value="">Seleziona utente</option>
                        {users.map((user) => {
                            const { id, name, username } = user;
                            return (
                                <option key={id} value={id}>
                                    {id} - {name} - {username}
                                </option>
                            );
                        })}
                    </select>
                </div>
                <div className="col-md-6">
                    <label className="form-label">Album</label>
                    <select
                        className="form-select"
                        value={selectedAlbum}
                        onChange={handleAlbumsChange}
                    >
                        <option value="">Seleziona album</option>
                        {albums.map((album) => {
                            const { userId, id, title } = album;
                            return (
                                <option key={id} value={id}>
                                    {userId} - {title}
                                </option>
                            );
                        })}
                    </select>
                </div>
            </div>

            <div className="row">
                <div className="col">
                    <div className="photo-list">
                        {photos.map((photo) => {
                            const { albumId, id, title } = photo;
                            return (
                                <div className="photo-card" key={id}>
                                    <p>
                                        <b>ID:</b> {id} <br />
                                        <b>AlbumID:</b> {albumId} <br />
                                        <b>Title:</b> {title}
                                    </p>
                                </div>
                            );
                        })}
                    </div>
                </div>
            </div>
        </div>
    );
};

const Loading = () => {
    return <h2 className="text-center text-primary mt-4">Loading...</h2>;
};

export default UserAlbums;