const URL = `http://localhost:3001/api/articles`

const fetchArticleByID = async (articleID) => {
  const res = await fetch(`${URL}/${articleID}`)
  const body = await res.json()
  return body
};

const fetchArticlesBySection = async (section) => {
  const res = await fetch(`${URL}?filter={"where":{"section":"${section}"}}`)
  const body = await res.json()
  return body
};

const fetchArticles = async (filters = null) => {
  const res = await fetch(`${URL}${filters !== null ? filters : ''}`)
  const body = await res.json()
  return body
};

const addArticle = async (newArticle) => {
  try {
    const res = await fetch(URL, {
      method: 'POST',
      headers: {
        'Content-type': 'application/json'
      },
      body: JSON.stringify(newArticle)
    })
    const data = await res.json()
    if (data.error) {
      return {
        'message': data.message, 'statusCode':200
      }
    } return data
  }
  catch (err) {
    console.log(err)
  }
}

export default {
  fetchArticleByID: fetchArticleByID,
  fetchArticles: fetchArticles,
  fetchArticlesBySection: fetchArticlesBySection,
  addArticle: addArticle
};
