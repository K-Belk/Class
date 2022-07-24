import React from 'react';
import moment from 'moment'
import { ListGroup } from 'react-bootstrap';

const ArticleTeaser = (props) => { 

  const {id, title, created_date, handleTitleClick} = props

  return (
    <div>
      <ListGroup.Item className="d-flex justify-content-between align-items-start"
      >
      <div className="ms-2 me-auto">
      <a href='#' onClick={(event) => {
        event.preventDefault()
        handleTitleClick(id)
      }}>{ title }</a>
      <div>{ moment(created_date).format( 'dddd MMMM Do, YYYY') }</div>
      </div>
      
      </ListGroup.Item>
      </div>
  )
}


export default ArticleTeaser;
