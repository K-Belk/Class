import React, { useState } from 'react';
import News from './data/news.json';
import navItemsJson from './data/navItems.json';
import './App.css';
import AppNav from './components/AppNav/AppNav.js';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import HomePage from './pages/HomePage';
import ArticlePage from './pages/ArticlePage'

const App = () => { 

  const  getNews = () => {
    
  }
  
  const [navItems, setNavItems] = useState(navItemsJson)

  return (
  <div>
    <h1>AppNav Component</h1>
    <hr />
    <AppNav navItems={navItems} handleNavClick={(clickedItem) => console.log(clickedItem)} />
    <Router>
      <div>
        <Routes>
          <Route path='/' element={<HomePage />} />
          <Route path='/articles/:articleID' element={<ArticlePage />} />
        </Routes>
      </div>
    </Router>
  </div>
);

}

export default App;
