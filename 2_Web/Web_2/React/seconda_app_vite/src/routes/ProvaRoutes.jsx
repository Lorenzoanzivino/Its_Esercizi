import React, { useState } from 'react';
import Home from './Home';
import About from './About';
import Profile from './Profile';

const ProvaRoutes = () => {
    const [link, setLink] = useState("Home");
    const renderComponent = () => {
        if (link === "Home") {
            return <Home></Home>;
        }
        if (link === "About") {
            return <About></About>;
        }
        if (link === "Profile") {
            return <Profile></Profile>;
        }
    };
    return (
        <div>
            <nav className="navbar bg-body-tertiary">
                <div className="container-fluid">
                    <button
                        className="btn btn-link nav-link"
                        onClick={() => setLink("Home")}
                    >
                        Home
                    </button>
                    <button
                        className="btn btn-link nav-link"
                        onClick={() => setLink("About")}
                    >
                        About
                    </button>
                    <button
                        className="btn btn-link nav-link"
                        onClick={() => setLink("Profile")}
                    >
                        Profile
                    </button>
                </div>
            </nav>
            <div className='container'>
                <br />
                <b>{renderComponent()}</b>
            </div>
        </div>
    );
};

export default ProvaRoutes;