import React, { Component } from 'react';
import ArticleList from '../components/ArticleList/ArticleList';
import News from '../data/news.json';
import { useNavigate } from 'react-router-dom';


const HomePage = (props) => {
  let navigate = useNavigate()
  return (
    <div>
      <ArticleList articles={News} handleTitleClick={(articleID) => navigate(`/articles/${articleID}`) } />
    </div>
  );

}

export default HomePage;
