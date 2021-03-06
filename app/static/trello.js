const mainDiv = document.getElementById('listbox')
const listAddButton = document.getElementById('addButton')
// const closeButton = document.getElementById('closeButton')
const listTitleDiv = document.getElementById('titleparent')

const addListLink = function () {
  const span = document.createElement('span')
  span.setAttribute('id', 'placeholder')
  span.textContent = '+ Add list'
  mainDiv.appendChild(span)
  span.addEventListener('click', createList)
}

const createList = function (e) {
  listTitleDiv.style.display = 'inline'
  mainDiv.style.backgroundColor = '#dfe3e6'
  e.target.style.display = 'none'
  listAddButton.addEventListener('click', checkListTitle)
  listAddButton.addEventListener('click', addAnotherList)

  // closeButton.addEventListener('click', listLinkAgain)
}
const addAnotherList = function () {
  // const main = document.querySelector('.container')
  const div2 = createElement('div', 'list2')
  const div1 = createList()
  div2.appendChild(div1)
  // main.appendChild(div2)
}

const checkListTitle = function () {
  const input = document.getElementById('inputForList')
  // console.log(input)
  if (input.value) {
    createListTitle(input.value)
    input.value = ''
    mainDiv.style.backgroundColor = '#dfe3e6'
  }
}

const createListTitle = function (listTitle) {
  const span = addListId(listTitle)
  listTitleDiv.style.display = 'none'
  mainDiv.style.backgroundColor = 'rgba(0,0,0,.12)'
  mainDiv.appendChild(span)
  createCardLink()
}

const createCardLink = function () {
  const span = createElement('span', 'createCard')
  const a = createElement('a', 'createCardLink')
  a.style.color = '#798d99'
  a.textContent = 'Add a card'
  span.appendChild(a)
  mainDiv.appendChild(span)
  span.addEventListener('click', createCard)
  // span.addEventListener('click', createList)
}

const createCard = function (e) {
  // console.log(e.target)
  e.target.style.display = 'none'
  const textArea = createElement('textarea', 'card')
  textArea.placeholder = 'Enter a title for this card...'
  const container = createElement('div', 'cardCreater')
  const button = createElement('button', 'addButton')
  button.setAttribute('id', 'addButton')
  button.innerHTML = 'Add card'
  const span = createElement('span', 'closeButton')
  span.setAttribute('id', 'closecard')
  span.innerHTML = '&times;'
  container.appendChild(textArea)
  container.appendChild(button)
  container.appendChild(span)
  span.addEventListener('click', closeCreateCard)
  mainDiv.insertBefore(container, mainDiv.lastChild)
  button.addEventListener('click', checkCard)
}

const closeCreateCard = function () {
  const div = document.getElementsByClassName('cardCreater') //  HTML collection
  console.log(div)
  div[0].style.display = 'none'
  createCardLink()
}

const checkCard = function () {
  const textArea = document.getElementsByClassName('card')
  if (textArea[0].value) {
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
        addCard(res.cards[0].title, res.cards[0].id)
        // addListId(res.list_id)
      })
    // const listTitle = document.getElementsByClassName('card')
    textArea[0].value = ''
  }
}

const addCard = function (cardTitle, id) {
  const card = createCardBox(cardTitle, id)
  displayCard(card)
}

const displayCard = function (card) {
  const listTitle = document.getElementById('title')
  listTitle.appendChild(card)
  document.getElementById('placeholder').style.display = 'none'
}

const deleteCard = function (e) {
  console.log(e.target.parentNode.parentNode.parentNode)
  const parent = document.getElementById('title')
  console.log(parent.childNodes[0])
  parent.removeChild(parent.childNodes[1])
  const cardDetails = { title: e.target.parentNode.textContent, list_id: '1', id: e.target.parentNode.id }
  const options = {
    method: 'DELETE',
    body: JSON.stringify(cardDetails),
    headers: {
      'Accept-Encoding': 'application/json',
      'Content-Type': 'application/json'
    }
  }

  fetch('http://localhost:5000/trillo/cards/' + e.target.parentNode.id, options)
    .then(res => res.json())
    .then(res => console.log(res))
}

const createCardBox = function (cardName, id) {
  const spanCard = createElement('span', 'cardSpan')
  const card = createElement('div', 'cardholder')
  card.setAttribute('id', 'card')
  spanCard.textContent = cardName
  spanCard.setAttribute('id', id)
  const i = createElement('i', 'fas fa-pencil-alt')
  const i2 = createElement('i', 'fas fa-trash-alt')
  spanCard.appendChild(i2)
  spanCard.appendChild(i)
  i.addEventListener('click', editCard)
  i2.addEventListener('click', deleteCard)
  // i2.addEventListener('click', deleteCard)
  card.appendChild(spanCard)
  return card
}

const editCard = function (e) {
  const update = document.querySelector('.updateTask')
  const span = e.target.parentNode
  const textArea = createElement('textArea', 'editFeild')
  textArea.textContent = span.textContent
  update.appendChild(textArea)
  update.classList.toggle('show-modal')
  const button = createElement('button', 'saveButton')
  button.setAttribute('id', span.id)
  button.textContent = 'save'
  update.appendChild(button)
  button.addEventListener('click', saveCard)
}

const saveCard = function (e) {
  const update = document.querySelector('.updateTask')
  // const textArea = document.querySelector('.editFeild')
  console.log(e.target.previousSibling)
  const textArea = e.target.previousSibling
  const span = document.getElementById(e.target.id)
  // console.log(span)
  span.textContent = textArea.value
  const i = createElement('i', 'fas fa-pencil-alt')
  const i2 = createElement('i', 'fas fa-trash-alt')
  span.appendChild(i)
  span.appendChild(i2)
  i.addEventListener('click', editCard)
  // console.log(span)
  const cardDetails = { title: textArea.value, list_id: '1' }
  const options = {
    method: 'PUT',
    body: JSON.stringify(cardDetails),
    headers: {
      'Accept-Encoding': 'application/json',
      'Content-Type': 'application/json'
    }
  }
  fetch('http://localhost:5000/trillo/cards/' + e.target.id, options)
    .then(res => res.json())
    .then(res => console.log(res))

  update.classList.toggle('show-modal')
}

const addListId = function (listId) {
  const span = createElement('span', 'listtitle')
  span.textContent = listId
  span.setAttribute('id', 'title')
  return span
}

const createElement = function (element, classVal) {
  const span = document.createElement(element)
  span.setAttribute('class', classVal)
  return span
}
// createListTitle('1')

// fetch('http://localhost:5000/trillo/cards')
//   .then(res => res.json())
//   .then(data => {
//     let items = data['cards']
//     // console.log(items)
//     for (let item in items) {
//       // console.log(items[item]['title'])
//       // console.log(items[item]['id'])
//       addCard(items[item]['title'], items[item]['id'])
//     }
//     document.getElementById('placeholder').style.display = 'none'
//     // console.log(data)
//   })

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
