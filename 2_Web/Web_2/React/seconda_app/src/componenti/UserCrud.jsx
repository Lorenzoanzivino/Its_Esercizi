import { useEffect, useState } from "react";

const urlUser = "https://jsonplaceholder.typicode.com/users";
const UserCrud = () => {
    const [users, setUsers] = useState([]);

    const getUsers = () => {
        fetch(urlUser)
            .then((response) => response.json())
            .then((ris) => setUsers(ris));
    };
    useEffect(() => {
        getUsers();
    }, []);
    return (
        <>
            <div className="container">
                <h1>USER CRUD</h1>
                <div>
                    {users.map((u) => {
                        return (
                            <div className="row">
                                <div className="col-8">{u.name}</div>
                                <div className="col-4">
                                    <button className="btn btn-primary">Update</button>
                                    <button className="btn btn-danger">Delete</button>
                                </div>
                            </div>
                        );
                    })}
                </div>
            </div>
        </>
    );
};

export default UserCrud;