import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import ArticlesAPI from '../api/ArticlesAPI'
import ArticleList from '../components/ArticleList/ArticleList'

const SectionPage = (props) => {
  let {sectionID} = useParams()
  const [articles, setArticles] = useState([])
  const [section, setSection] = useState(null)

  if (sectionID !== section) {
    setSection(sectionID)
  }

  useEffect(() => {
    const getSectionArticles = async () => {
      try {
        if (section) {
          const theSection = await ArticlesAPI.fetchArticlesBySection(section)
          setArticles(theSection)
        }
      }
      catch {
        console.error('Error ocurred fetching articles', error)
      }
    }
    getSectionArticles()
  }, [section])

  return (
    <div>
      <h1>{ section } </h1>
      {<ArticleList articles={ articles } />}
      
    </div>
  )
}

export default SectionPage
