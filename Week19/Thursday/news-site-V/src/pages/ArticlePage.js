import React, { Component, useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import ArticlesAPI from '../api/ArticlesAPI.js';
import Article from '../components/Article/Article.js'

const ArticlePage = () => {
  let { articleID } = useParams()

  const [article, setArticle] = useState()

  useEffect(() => {
    const getArticle = async () => {
      try{
        const theArticle = await ArticlesAPI.fetchArticleByID(articleID)
        setArticle(theArticle)
      }
      catch(error) {
        console.error('Error ocurred fetching article', error)
      }
    }
    getArticle()
  }, [])

  return (
    <div>
      <Article {...article}/>
    </div>
  )
}

export default ArticlePage;
