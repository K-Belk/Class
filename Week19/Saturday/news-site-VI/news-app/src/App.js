import React, { useState } from 'react';
import navItemsJson from './data/sections.json';
import './App.css';
import AppNav from './components/AppNav/AppNav.js';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import HomePage from './pages/HomePage';
import ArticlePage from './pages/ArticlePage'
import SectionPage from './pages/SectionPage';
import SearchPage from './pages/SearchPage'
import AddArticlePage from './pages/AddArticlePage'
import LoginPage from './pages/LoginPage'
import 'bootstrap/dist/css/bootstrap.min.css';
import UserContextProvider from './contexts/UserContext';

const App = () => { 

  const [user, setUser] = useState(null)

  const handleLogin = (user) => {
    setUser(user)
  }

  const renderLoginPage = (props) => {
    return (
      <LoginPage 
      history={props.history}
      handleLogin={handleLogin} />
    )
  }

  return (
  <div>
    <Router>
      <div>
      <UserContextProvider >
        <AppNav navItems={navItemsJson} />
          <Routes>
            <Route path='/' element={<HomePage />} />
            <Route path='/articles/:articleID' element={<ArticlePage />} />
            <Route path="/section/:sectionID" element={<SectionPage />} />
            <Route path="/search/:searchQuery" element={<SearchPage />} />
            <Route path="/add-article" element={<AddArticlePage />} />
            <Route path="/login" element={<LoginPage />} />
          </Routes>
        </UserContextProvider>
      </div>
    </Router>
  </div>
);

}

export default App;