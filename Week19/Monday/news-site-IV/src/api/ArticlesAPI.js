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

export default {
  fetchArticleByID,
  fetchArticles,
  fetchArticlesBySection
};
