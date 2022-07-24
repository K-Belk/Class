import React from 'react';
import {Navbar, Nav, Form, FormControl, Button} from 'react-bootstrap'
import { useNavigate } from 'react-router-dom';
import sections from '../../config/Sections.json'



const AppNav = (props) => { 

let navigate = useNavigate()

  const displayDemNavItems = () => { 
    
    return sections.map((navItem, idx) => {
      return <Nav.Link key={idx} onClick={() => navigate(`section/${navItem.value}`)}> {navItem.label} </Nav.Link>
    })
  }

  const handleSearch = (event) => {
    event.preventDefault()
    let searchQuery = event.target.search.value
    return navigate(`search/${searchQuery}`)
    }
  

  return (
    <Navbar bg='dark' variant='dark' >
      <Navbar.Brand href="/">The News Site</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className='mr-auto'>
            {displayDemNavItems()}
            </Nav>
          </Navbar.Collapse>
          <Form className="d-flex m-2" onSubmit={handleSearch} >
          <FormControl
            type="search"
            placeholder="Search"
            className="me-2"
            aria-label="Search"
            name='search'
          />
          <Button variant="outline-info" type='submit'>Search</Button>
        </Form>
    </Navbar>
  )
}


export default AppNav;
