import React from "react";
import "./Loader.css";

const Loader = () => {
    return (
        <div className="loader-overlay">
            <div className="loader"></div>
            <div className="loader-text">Loading...</div>
        </div>
    );
};

export default Loader;
