
import Header from './components/Header/Header'
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Register from './components/Register/Register'
import Login from "./components/Login/Login";
import Properties from "./components/Properties";
import About from "./components/About";
import Home from "./components/Home/Home"

import './App.css'

function App() {
 

  return (
    <>
      <BrowserRouter>
        <Header />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<Login />} />
          <Route path="/properties" element={<Properties />} />
          <Route path="/About" element={<About />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App
