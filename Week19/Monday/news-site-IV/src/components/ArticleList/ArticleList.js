import React from 'react';
import { ListGroup } from 'react-bootstrap';
import ArticleTeaser from '../ArticleTeaser/ArticleTeaser';


const ArticleList = (props) => {

  const {articles, handleTitleClick} = props

  const ArticleTeaserList = (articles ) => {
    return articles.map((article,idx) => <ArticleTeaser
    key={idx}
    id={idx+1}
    title={article.title}
    created_date={article.created_date}
    handleTitleClick={handleTitleClick}/>)
  }


  return (
      <div>
        <ListGroup >
          {ArticleTeaserList(articles)}
        </ListGroup>
      </div>
    );
}


export default ArticleList;
