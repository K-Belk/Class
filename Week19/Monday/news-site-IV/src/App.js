import React from 'react';
import navItemsJson from './data/sections.json';
import './App.css';
import AppNav from './components/AppNav/AppNav.js';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import HomePage from './pages/HomePage';
import ArticlePage from './pages/ArticlePage'
import SectionPage from './pages/SectionPage';
import SearchPage from './pages/SearchPage'
import 'bootstrap/dist/css/bootstrap.min.css';

const App = () => { 

  return (
  <div>
    <Router>
      <div>
        <AppNav navItems={navItemsJson} />
          <Routes>
            <Route path='/' element={<HomePage />} />
            <Route path='/articles/:articleID' element={<ArticlePage />} />
            <Route path="/section/:sectionID" element={<SectionPage />} />
            <Route path="/search/:searchQuery" element={<SearchPage />} />
          </Routes>
      </div>
    </Router>
  </div>
);

}

export default App;