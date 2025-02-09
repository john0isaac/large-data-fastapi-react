import React, { useEffect, useState } from "react";
import logo from "./logo.svg";
import "./App.css";
import Loader from "./components/Loader/Loader";

import { DataService, FilesService, OpenAPI } from "./generated/openapiclient/";

import { FixedSizeList } from "react-window";

const App = () => {
    OpenAPI.BASE = "http://localhost:8000";
    const [isLoading, setIsLoading] = useState(false);
    const [files, setFiles] = useState([]);
    const [selectedFile, setSelectedFile] = useState(null);

    const [data, setData] = useState([]);

    const Row = ({ index, style }) => (
        <div
            style={{
                ...style,
                textOverflow: "ellipsis",
                overflow: "hidden",
                border: "1px solid black",
                borderRadius: "0.5rem",
                backgroundColor: "gray",
                margin: "0.5rem"
            }}
            key={index}
            title={data[index].description}
        >
            {data[index].description}
        </div>
    );

    const fetchFiles = async () => {
        FilesService.getDataFilenamesFilenamesGet()
            .then(response => {
                console.log(response);
                setFiles(response);
            })
            .catch(error => {
                console.error(error);
            });
    };

    const handleFileChange = event => {
        setSelectedFile(event.target.value);
    };

    const handlePopulateClick = async () => {
        setIsLoading(true);
        DataService.populateDataDataPopulateFileNameGet(selectedFile)
            .then(response => {
                console.log(response);
                setIsLoading(false);
            })
            .catch(error => {
                console.error(error);
                setIsLoading(false);
            });
    };

    const handelGetData = async () => {
        setIsLoading(true);
        DataService.getDataDataGet()
            .then(response => {
                setData(response);
                setIsLoading(false);
            })
            .catch(error => {
                console.error(error);
                setIsLoading(false);
            });
    };

    useEffect(() => {
        fetchFiles();
    }, []);
    return (
        <div className="App">
            {isLoading && <Loader />}
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>
                    Select a file to populate the database with: <br />
                    <select onChange={handleFileChange}>
                        {files &&
                            files.map(file => {
                                return <option key={file}>{file}</option>;
                            })}
                    </select>
                    <button onClick={handlePopulateClick}>Populate</button>
                </p>
                <p>
                    Get the data from the database: <br />
                    <button onClick={handelGetData}>Get Data</button>
                </p>
                <p>
                    <FixedSizeList height={150} itemCount={data.length || 0} itemSize={35} width={300}>
                        {Row}
                    </FixedSizeList>
                </p>
                <a className="App-link" href="https://github.com/john0isaac/large-data-fastapi-react" target="_blank" rel="noopener noreferrer">
                    Checkout the GitHub repository
                </a>
            </header>
        </div>
    );
};

export default App;
