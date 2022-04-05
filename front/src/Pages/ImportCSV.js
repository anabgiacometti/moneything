import React from "react";
import { Link } from "react-router-dom";

const Import = () => {
  return (
    <div>
      <h1>Import</h1>
      <nav>
        <ul>
          <li>
            <Link to="/">Sobre</Link>
          </li>
          <li>
            <Link to="/dashboard">Usuario</Link>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default Import;
