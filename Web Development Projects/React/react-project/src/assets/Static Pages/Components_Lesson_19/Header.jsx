export default function Header() {
    return (
      <header className="header">
        <img className="img" src="../public/react-logo.png" alt="React logo" />
        <nav className="nav-list">
          <ul className="nav-list">
            <li className="nav-list-items">Pricing</li>
            <li className="nav-list-items">About</li>
            <li className="nav-list-items">Contact</li>
          </ul>
        </nav>
      </header>
    );
  }