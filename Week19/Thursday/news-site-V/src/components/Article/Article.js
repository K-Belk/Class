import React from 'react';
import moment from 'moment'
import { Card } from 'react-bootstrap';

const Article = (props) => { 

  const {title, created_date, abstract, byline, image} = props
  return (
    <div>
      <Card style={{ width: '25rem' }}>
        { image && <Card.Img src={ image }></Card.Img>}
        <Card.Body>
          <Card.Title>{ title }</Card.Title>
          { byline && <div>{ byline }</div>}
            <div>{ moment(created_date).format( 'dddd MMMM Do, YYYY') }</div>
              <Card.Text>
                <div> { abstract }</div>
              </Card.Text>
        </Card.Body>
      </Card>
    </div>
  )
}

export default Article;
