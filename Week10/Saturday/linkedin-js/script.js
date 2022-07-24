const title = document.getElementById('title')
const aboutMe = document.getElementsByClassName('about-me')
const userName = document.querySelector('.name')
const job = document.querySelectorAll('.job')

console.log(title)
console.log(aboutMe)
console.log(userName)
console.log(job)

console.log(job[2])

job[0].innerHTML = 'Molex 2014 - present'
job[5].remove()
title.style.fontWeight = 10
title.style.fontSize = '16px'

userName.addEventListener('click', function(){alert('Thats my name')})
userName.style.cursor = 'pointer'

const allowDrop = (ev) => {
  ev.preventDefault()
}

const drag = (ev) => {
  ev.dataTransfer.setData('text', ev.target.id)
}

const drop = (ev) => {
  ev.preventDefault()
  let data = ev.dataTransfer.getData('text')
  ev.target.appendChild(document.getElementById(data))
}

job.forEach(element => {
  element.draggable='true'
  element.ondragstart='drag(event)'
  element.ondrop='drop(event)'
  element.ondragover='allowDrop(event)'
})