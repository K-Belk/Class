import React, { Component } from 'react';
import { useParams } from 'react-router-dom';
import Article from '../components/Article/Article.js'
import News from '../data/news.json';

const ArticlePage = () => {
  let { articleID } = useParams()
  const article = News[articleID - 1]
  return (
    <div>
      <Article {...article}/>
    </div>
  )
}

export default ArticlePage;
