import React from 'react';

const Article = (props) => { 

  const {title, created_date, abstract, byline, image} = props
  return (
    <div>
      <h1>{ title }</h1>
      <p>{ created_date }</p>
      { byline && <h2>{ byline }</h2>}
      { image && <img src={ image }></img>}
      <p>abstract { abstract }</p>
      

    </div>
  )
}

export default Article;
