const buttonPressed = document.getElementById('submit-button')
const enteredUsername = document.getElementById('username')
const enterUsername = document.getElementById('enter-username')
const welcome = document.getElementById('welcome-message')


buttonPressed.addEventListener('click', function () {
  addUsername()
  welcomeMessage()
  hideShow()
})

const addUsername = () => {localStorage.setItem('username', enteredUsername.value)}

const hideShow = () => {

  if (localStorage.getItem('username').length > 1) {
    enterUsername.style.display = 'none'
  } else {
    enterUsername.style.display = 'block'
  }
}

const welcomeMessage = () => {
  const message = document.createElement('div')
  message.id = 'message'
  message.innerText = `Welcome ${localStorage.getItem('username')}`
  welcome.appendChild(message)
}

if (localStorage.getItem('username')){
  welcomeMessage()
  hideShow()
}
