import { Route, Routes, BrowserRouter } from "react-router-dom";
import Dashboard from "./Pages/Dashboard";
import ImportCSV from "./Pages/ImportCSV";

function App() {
  return (
    <BrowserRouter>
      {/* <div className="App">
        <Link to="/">Home</Link>
        <Link to="/category">About</Link>
      </div> */}
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/import-csv" element={<ImportCSV />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
