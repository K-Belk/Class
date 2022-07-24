import React from 'react';

const Article = (props) => { 

  const {title, created_date, abstract, byline, multimedia} = props
  const image = multimedia.length ? multimedia[0].url : null
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
