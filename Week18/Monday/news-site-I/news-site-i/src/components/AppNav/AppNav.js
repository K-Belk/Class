import React from 'react';
import Navbar from 'react-bootstrap/Navbar'

const AppNav = (props) => { 

  const {navItems, handleNavClick} = props

  const displayDemNavItems = () => { 
    return navItems.map((navItem, idx) => {
      return <a key={idx+1} onClick={() => handleNavClick(navItem.value)}> {navItem.label} </a>
    })
  }

  return (
    <Navbar >
    <Navbar.Brand>The News Site</Navbar.Brand>
      <nav className="me-auto">
      {displayDemNavItems()}
      </nav>
    </Navbar>
  )
}


export default AppNav;
