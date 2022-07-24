import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom';
import ArticlesAPI from '../api/ArticlesAPI';
import ArticleList from '../components/ArticleList/ArticleList';


const SearchPage = (props) => {
  let { searchQuery } = useParams()
  const [articles, setArticles] = useState([])
  const [message, setMessage] = useState(null);


  useEffect(() => {
    let filter = `?filter={"where":{"title":{"ilike":"${searchQuery}"}}}`
    if (searchQuery.length) {
      const getSearchResults = async () => {
        try {
          const searchResults = await ArticlesAPI.fetchArticles(filter)
          setArticles(searchResults)
          setMessage(`You're search returned ${searchResults.length} results`)
        }
        catch(error){
          console.error('Aww Snap, There is an error',error)
        }
      }
      getSearchResults()
      console.log(articles)
      }
  }, [])

  // console.log(searchQuery)

  return (
    <div>
    {<ArticleList articles={articles}  />}
    </div>
  )
}

export default SearchPage