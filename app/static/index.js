// console.log('hello')
// const button = document.getElementById('button')
// let modal = document.getElementById('page-modal')

// button.onclick = function () {
//   modal.style.display = 'block'
// //    const menu = document.createElement('div')
// //    menu.setAttribute('class', 'popbox')
// }
// const closeButton = document.getElementById('close')

// closeButton.onclick = function () {
//   modal.style.display = 'none'
// }

// const board = document.getElementById('board')
// board.onclick = function () {
//  let div = document.createElement('div')
//  div.setAttribute('class', 'boardBox') 
//  let holder = document.getElementById('title-div')
//  let text = document.createTextNode('Add board title')
//  text.onmouseover = inputFunction(e)
//  div.appendChild(text)
//  holder.appendChild(div)
// }
// const inputFunction = function (e) {
//   let input = document.createElement('input')
//   input.setAttribute('placeholder', 'Add board title')
//   e.target.appendChild(input)
// }

// console.log(listBox) 

const getAllCards = async (url) => {
  const response = await fetch(url)
  const tasks = await response.json()
  return tasks
}

const start = async function () {
  state = await getAllCards('http://localhost:5000/trillo/cards')
  displayTask(state)
}


const createList = function (e) {
  e.target.style.display = 'none'
  const container = document.createElement('div')
  const input = document.createElement('input')
  const button = document.createElement('button')
  const span = document.createElement('span')
  const listBox = document.getElementById('listbox')
  const parent = document.createElement('div')
  container.setAttribute('class', 'containerBox')
  input.setAttribute('placeholder', 'Enter list title...')
  button.innerHTML = 'Add list'
  span.innerHTML = '&times;'
  button.setAttribute('class', 'addButton')
  span.setAttribute('class','closeButton')
  parent.appendChild(input)
  container.appendChild(button)
  container.appendChild(span)
  parent.appendChild(container)
  listBox.appendChild(parent)
 

  // console.log(e.target)
  
  listBox.style.backgroundColor = '#dfe3e6';
  button.addEventListener('click', createListTitle)
  

}
const span = document.getElementById('placeholder')
span.addEventListener('click',createList)

const createListTitle = function (e) {
  const removeItems = e.target.parentNode.parentNode
  const input = removeItems.firstChild
  const emptyDiv = document.createElement('div')
  emptyDiv.setAttribute('class', 'emptyDiv')
  // console.log(input.value)
  if(input.value) {
  removeItems.style.display = 'none'
  const span = document.createElement('span')
  span.innerHTML = input.value
  span.setAttribute('class', 'listtitle')
  span.setAttribute('id', 'title')
  removeItems.parentNode.appendChild(span)
  removeItems.parentNode.appendChild(emptyDiv)
  const span2 = document.createElement('span')
  span2.setAttribute('class', 'createCard')
  const a = document.createElement('a')
  a.textContent = 'Add a card'
  span2.appendChild(a)
  removeItems.parentNode.appendChild(span2)
  // console.log(removeItems.innerHTML)
  span2.addEventListener('click', createCard)
  } 
}

const createCard = function (e) {
  // console.log(e.target)
  e.target.style.display = 'none'
  // console.log(e.target.parentNode)
  const textArea = document.createElement('textarea')
  textArea.setAttribute('class', 'card')
  textArea.placeholder = 'Enter a title for this card...'
  e.target.parentNode.parentNode.insertBefore(textArea, e.target.parentNode.parentNode.lastChild)
  const container = document.createElement('div')
  const button = document.createElement('button')
  button.setAttribute('class', 'addButton')
  button.innerHTML = 'Add card'
  const span = document.createElement('span')
  span.innerHTML = '&times;'
  span.setAttribute('class','closeButton')
  container.appendChild(button)
  container.appendChild(span)
  e.target.parentNode.parentNode.insertBefore(container, e.target.parentNode.parentNode.lastChild)
  button.addEventListener('click', addCard)

}

const addCard = function () {
  let newCard = cardBox()
  const listTitle = document.getElementById('title')
  // console.log()
  listTitle.appendChild(newCard)
  // mainDiv.insertad(card, listTitle)
  console.log('main-->'+mainDiv)
  // mainDiv.firstChild.insertAdjacentElement('afterend', spancard);
  // createCardLink.style.display = 'none'
}
 const cardBox = function () {
  const textArea = document.getElementsByClassName('card')
  if(textArea[0].value) {
  const listTitle = document.getElementsByClassName('card')
  const spancard = document.createElement('span')
  const createCardLink = document.getElementsByClassName('createCard')
  // console.log(textArea[0].value)
  const card = document.createElement('div')
  card.setAttribute('class', 'cardholder')
  spancard.innerHTML = textArea[0].value
  textArea[0].value = ''
  console.log(spancard)
  card.appendChild(spancard)
  console.log(card)
  return card
  }
 }


