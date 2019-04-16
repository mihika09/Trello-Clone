'use strict'
const mainDiv = document.getElementById('listbox')
const listAddButton = document.getElementById('addButton')
// const closeButton = document.getElementById('closeButton')
const listTitleDiv = document.getElementById('titleparent')

// let obj = { items: [
//   { description: 'test', id: 'a1065c22-', list_id: '1', title: 'card#C10' },
//   { description: 'test', id: 'cdd606e4-', list_id: '1', title: 'card#C1000000' }]
// }

const createElement = function (element, classVal) {
  const span = document.createElement(element)
  span.setAttribute('class', classVal)
  return span
}

const addListId = function (listId) {
  const span = createElement('span', 'listtitle')
  span.textContent = listId
  span.setAttribute('id', 'title')
  return span
}

const editCard = function (e) {
const card = document.getElementById
}

const createCardBox = function (cardName, id) {
  const spanCard = document.createElement('span')
  const card = createElement('div', 'cardholder')
  card.setAttribute('id', 'spanCard')
  spanCard.innerHTML = cardName
  spanCard.setAttribute('id', id)
  console.log(spanCard)
  const i = createElement('i', 'fas fa-pencil-alt')
  spanCard.appendChild(i)
  i.addEventListener('click', editCard)
  card.appendChild(spanCard)
  console.log(card)
  return card
}

const displayCard = function (card) {
  const listTitle = document.getElementById('title')
  listTitle.appendChild(card)
  // mainDiv.insertad(card, listTitle)
  // mainDiv.firstChild.insertAdjacentElement('afterend', spancard);
  // createCardLink.style.display = 'none'
}

const addCard = function (cardTitle) {
  const card = createCardBox(cardTitle)
  displayCard(card)
}

const checkCard = function () {
  const textArea = document.getElementsByClassName('card')
  if (textArea[0].value) {
    addCard(textArea[0].value)
    const cardDetails = { title: textArea[0].value, list_id: '1' }
    const options = {
      method: 'POST',
      body: JSON.stringify(cardDetails),
      headers: {
        'Accept-Encoding': 'application/json',
        'Content-Type': 'application/json'
      }
    }

    fetch('http://localhost:5000/trillo/cards', options)
      .then(res => res.json())
      .then(res => {
        console.log(res)
      // addListId(res.list_id)
      })
    // const listTitle = document.getElementsByClassName('card')
    textArea[0].value = ''
  }
}

const createCard = function (e) {
  // console.log(e.target)
  e.target.style.display = 'none'
  // console.log(e.target.parentNode)
  const textArea = createElement('textarea', 'card')
  // textArea.setAttribute('class', 'card')
  textArea.placeholder = 'Enter a title for this card...'
  e.target.parentNode.parentNode.insertBefore(textArea, e.target.parentNode.parentNode.lastChild)
  const container = document.createElement('div')
  const button = createElement('button', 'addButton')
  button.setAttribute('id', 'addButton')
  button.innerHTML = 'Add card'
  const span = document.createElement('span')
  span.innerHTML = '&times;'
  span.setAttribute('class', 'closeButton')
  container.appendChild(button)
  container.appendChild(span)
  e.target.parentNode.parentNode.insertBefore(container, e.target.parentNode.parentNode.lastChild)
  button.addEventListener('click', checkCard)
}

const createListTitle = function (listTitle) {
  const span = addListId(listTitle)
  listTitleDiv.style.display = 'none'
  mainDiv.style.backgroundColor = 'rgba(0,0,0,.12)'
  mainDiv.appendChild(span)
  const span2 = createElement('span', 'createCard')
  const a = createElement('a', 'createCardLink')
  a.style.color = '#798d99'
  a.textContent = 'Add a card'
  span2.appendChild(a)
  mainDiv.appendChild(span2)
  span2.addEventListener('click', createCard)
}

createListTitle('1')

fetch('http://localhost:5000/trillo/cards')
  .then(res => res.json())
  .then(data => {
    let items = data['items']
    console.log(items)
    for (let item in items) {
      // console.log(items[item]['title'])
      console.log(item)
      addCard(items[item]['title'])
    }
    console.log(data)
  })

const checkListTitle = function () {
  const input = document.getElementById('inputForList')
  console.log(input)
  if (input.value) {
    createListTitle(input.value)
    input.value = ''
    mainDiv.style.backgroundColor = '#dfe3e6'
  }
}
const createList = function (e) {
  listTitleDiv.style.display = 'block'
  mainDiv.style.backgroundColor = '#dfe3e6'
  e.target.style.display = 'none'
  listAddButton.addEventListener('click', checkListTitle)
  // closeButton.addEventListener('click', listLinkAgain)
}

const addListLink = function () {
  const span = document.createElement('span')
  span.setAttribute('id', 'placeholder')
  span.textContent = '+ Add list'
  mainDiv.appendChild(span)
  span.addEventListener('click', createList)
}
addListLink()

// const listLinkAgain = function (e) {
//   listTitleDiv.style.display = 'none'
//   mainDiv.style.backgroundColor = 'rgba(0,0,0,.12)'
//   mainDiv.firstChild.display = 'block'
//   addListLink()
// }

// state = [{cards: [ { id:'1',title: 'card01'}]}]
// console.log(state[0]['cards'][0]['id'])
// for(let item of state) {
//   const card = createCardBox(item['cards'][0]['title'])
//   displayCard(card)
// }

// listAddButton.addEventListener('click', createListTitle)
