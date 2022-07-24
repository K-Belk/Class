import React, { useState }from 'react'
import { Form, Button } from 'react-bootstrap'
import { useNavigate } from 'react-router-dom'
import ArticlesAPI from '../api/ArticlesAPI'
import sections from '../data/sections.json'




const AddArticlePage = () => {
  const navigate = useNavigate()
  const [message, setMessage] = useState(null)

  const sectionsMenu = () => { 
    return sections.map((section, idx) => {
      return <option  key={idx} value={section.value} > {section.value} </option>
    })
  }

  const handleSubmit = async (event) => {
    event.preventDefault()
    const newArticle = {
      'title': event.target.title.value,
      'byline': event.target.byline.value,
      'abstract': event.target.abstract.value,
      'section': event.target.section.value
    }
    let res = await ArticlesAPI.addArticle(newArticle)
    console.log(res)
    if (res.message) {
      setMessage(res.message)
    } else {
      navigate(`/articles/${res.id}`)
    }
  }

  return (
    <div>
      <Form onSubmit={handleSubmit}>
        <Form.Group className="m-3" >
          <Form.Label>Title</Form.Label>
          <Form.Control type="text" placeholder="Enter Title" name='title' />
        </Form.Group>

        <Form.Group className="m-3" >
          <Form.Label>Byline</Form.Label>
          <Form.Control type="text" placeholder="Enter Byline" name='byline' />
        </Form.Group>

        <Form.Group className="m-3" >
          <Form.Label>Abstract</Form.Label>
          <Form.Control type="textarea" placeholder="Enter Abstract" name='abstract' />
        </Form.Group>
        
        <Form.Group className="m-3" >
          <Form.Label>Section</Form.Label>
          <Form.Control as='select' placeholder='Section' name='section'>
            {sectionsMenu()}
          </Form.Control>
        </Form.Group>

        <Button variant="primary" type="submit">
          Submit
        </Button>
      </Form>
    </div>
  )
}

export default AddArticlePage