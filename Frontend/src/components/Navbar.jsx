import { NavLink } from "react-router-dom";

function Navbar() {
  return (
    <header className="navbar">
      <div className="brand">
        <span className="brand-icon">AI</span>

        <div>
          <h1>AI Chat Project</h1>
          <p>React + FastAPI + MySQL + OpenAI</p>
        </div>
      </div>

      <nav>
        <NavLink to="/">Home</NavLink>
        <NavLink to="/about">About</NavLink>
      </nav>
    </header>
  );
}

export default Navbar;