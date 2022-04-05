import { Route, Routes, BrowserRouter } from "react-router-dom";
import Home from "./Pages/Home";
import Dashboard from "./Pages/Dashboard";
import Category from "./Pages/Category";

function App() {
  return (
    <BrowserRouter>
      {/* <div className="App">
        <Link to="/">Home</Link>
        <Link to="/category">About</Link>
      </div> */}
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/category" element={<Category />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
