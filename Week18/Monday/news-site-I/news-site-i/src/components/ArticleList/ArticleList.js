import React from 'react';
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
        {ArticleTeaserList(articles)}
      </div>
    );
}


export default ArticleList;
