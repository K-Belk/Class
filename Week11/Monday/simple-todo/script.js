const listItems = document.getElementsById('list-items')
const enterButton = document.getElementById('enter-button')

let itemCount = 0

enterButton.addEventListener('click', function () {
  addItem()
  displayItem()
})

const addItem = () => {
  const newItem = document.getElementById('new-item')
  itemCount += 1
  localStorage.setItem(`${itemCount}`, newItem.value)
}

const displayItem = () => {
  const item = document.createElement('div')
  item.id = 'item'
  item.innerText = localStorage.getItem(`${itemCount}`)
  listItems.appendChild(item)
}

// JSON.parse(list)