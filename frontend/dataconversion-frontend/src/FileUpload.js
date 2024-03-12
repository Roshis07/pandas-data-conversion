import React, { useState } from 'react';
import axios from 'axios';
import './FileUpload.css';

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [responseData, setResponseData] = useState(null);
  const [error, setError] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleRemoveFile = () => {
    setFile(null);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const formData = new FormData();
      formData.append('file', file);

      const response = await axios.post('http://127.0.0.1:8000/data/infer/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      setResponseData(response.data);
      setError(null);
    } catch (error) {
      console.error('Error:', error);
      setError('An error occurred while processing the file.');
      setResponseData(null);
    }
  };

  const mapDataType = (dataType) => {
  if (dataType === 'datetime64[ns]' || dataType === 'timedelta64[ns]') {
    return 'Date';
  } else if (dataType === 'object') {
    return 'Text';
  } else if (dataType.includes('float')) {
    return 'Number';
  } else if (dataType.includes('int')) {
    return 'Number';
  }
  return dataType;
};
  return (
    <div className="container">
      <h1 className="header">Data Conversion Software</h1>
      <div className="content">
        <h2 className="title">Upload a File</h2>
        <form onSubmit={handleSubmit} className="form">
          <label htmlFor="file-upload" className="custom-file-upload">
            {file ? file.name : 'Choose File'}
            <input id="file-upload" type="file" onChange={handleFileChange} />
          </label>
          {file && (
            <button type="button" onClick={handleRemoveFile} className="remove-button">
              Remove
            </button>
          )}
          <button type="submit" className="upload-button">
            Upload
          </button>
        </form>

        {responseData && (
          <div>
            <h2>Data Types:</h2>
            <table className="response-table">
              <thead>
                <tr className="top-row">
                  <th>Column Name</th>
                  <th>Data Type</th>
                </tr>
              </thead>
              <tbody>
                {Object.entries(responseData).map(([column, dataType], index) => (
                  <tr key={column} className={index % 2 === 0 ? 'even-row' : 'odd-row'}>
                    <td>{column}</td>
                    <td>{mapDataType(dataType)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {error && (
          <div className="error">
            <p>Error: {error}</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default FileUpload;
