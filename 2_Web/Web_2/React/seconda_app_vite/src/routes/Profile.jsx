import React from 'react'
import { Link, Outlet } from 'react-router-dom';

const Profile = () => {
    return (
        <div>
            <br />
            <h1 className="text-center">Profile Page</h1>
            <br />
            <nav className='d-flex flex-row gap-2 justify-content-center'>
                <Link to="me">Il mio profilo (me)</Link>
                <Link to="/profile/2">Il mio profilo 2</Link>
            </nav>
            <br />
            <div>
                <nav className='d-flex flex-row gap-2 justify-content-center'>
                    <Outlet></Outlet>
                </nav>
            </div>
        </div>
    )
}
export default Profile;