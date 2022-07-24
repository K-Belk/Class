var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  "author": "kevin",
  "title": "post",
  "content": "test post"
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  mode: 'no-cors', // fixes the cors error
  body: raw,
  redirect: 'follow'
};

fetch("http://localhost:9291/posts", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));