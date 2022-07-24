import React, { Component, useEffect, useState } from 'react';
import ArticleList from '../components/ArticleList/ArticleList';
import { useNavigate } from 'react-router-dom';
import ArticlesAPI from '../api/ArticlesAPI'



const HomePage = (props) => {
  let navigate = useNavigate()
  const [articles, setArticles] = useState([])

  useEffect(() => {
    const getNews = async () => {
      try{
        const news = await ArticlesAPI.fetchArticles()
        setArticles(news)
      }
      catch{
        console.error('Error has ocurred fetching the list of articles', error)
      }
    }
    getNews()
  }, [])
  return (
    <div>
      <ArticleList articles={articles} handleTitleClick={(articleID) => navigate(`/articles/${articleID}`) } />
    </div>
  );

}

export default HomePage;
