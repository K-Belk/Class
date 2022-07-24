import React from 'react';

const ArticleTeaser = (props) => { 

  const {id, title, created_date, handleTitleClick} = props

  return (
    <div>
      <a href='#' onClick={(event) => {
        event.preventDefault()
        handleTitleClick(id)
      }}>{ title }</a>
      <p>{ created_date }</p>
    </div>
  )
}


export default ArticleTeaser;
