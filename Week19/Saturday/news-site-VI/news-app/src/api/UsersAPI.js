const login = async (credentialsObject, token) => {
  console.log(credentialsObject)
  try {
    const res = await fetch('http://localhost:3001/api/users/login?include=user', {
    method: 'POST',
    headers: {
      'Content-type': 'application/json',
    },
    body: JSON.stringify(credentialsObject)
  })
    const data = await res.json()
    return data
  }
  catch (error) {
    console.log(error)
  }
}



export default login