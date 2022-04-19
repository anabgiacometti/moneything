import { Route, Routes, BrowserRouter } from "react-router-dom";
import PageBase from "./Components/PageBase/Index";
import Dashboard from "./Pages/Dashboard";
import ImportCSV from "./Pages/ImportCsv/Index";

function App() {
  return (
    <BrowserRouter>
      <PageBase>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/import-csv" element={<ImportCSV />} />
        </Routes>
      </PageBase>
    </BrowserRouter>
  );
}

export default App;
