/* 
LINK: https://medium.com/@renanbastos93/criando-um-sistema-de-pagina%C3%A7%C3%A3o-simples-com-javascript-d2dd853741ea
items - Array dos Itens da Página;
pageActual - Número da Página a Ser Acessada;
limitItems - Limite de Ítens na Página.

function listItems(items, pageActual, limitItems){
    let result = []
    let totalPage = Math.ceil(items.length / limitItems)
    let count = (pageActual * limitItems) - limitItems
    let delimiter = count + limitItems
    if(pageActual <= totalPage){
        for(let i = count; i < delimiter; i++){
            result.push(items[i])
            count++
        }
    }
    return result
}

let next = ['t1', 't2', 't3', 't4', 't5', 't6', 't7']

console.log(listItems(next, 1, 2));
console.log(listItems(next, 2, 2));
console.log(listItems(next, 3, 2));
console.log(listItems(next, 3, 2));
console.log(listItems(next, 4, 2));
console.log(listItems(next, 1, 2));
*/
let ids = document.querySelectorAll('tr')
let pages = document.querySelector('.pages')
let pageActual = 1
let limitItems = 5

function hideAllItems(specificItemsArray = null){
    if(specificItemsArray !== null){
        for(let i of specificItemsArray){
            i.style.display = 'none'
        }
    }else{
        for (let item of getItems()){
            item.style.display = 'none'
        }
    }
}hideAllItems()

function createPages(items, limitItems){
    let totalPages = Math.ceil((items.length - 1) / limitItems)
    for(let i = 0; i < totalPages; i++){
        let page = document.createElement('div')
        page.className = 'page'
        page.innerHTML = i + 1
        pages.appendChild(page)
    }
    console.log(totalPages);
}createPages(getItems(), limitItems)
let pageClick = document.querySelectorAll('.page')
for (let pg of pageClick){
    pg.addEventListener('click', () => {
        console.log(pg.innerHTML);
    })
}

function listItems(items=getItems(), pageActual=1, limitItems=10){
    let result = []
    let totalPage = Math.ceil(items.length / limitItems)
    let count = (pageActual * limitItems) - limitItems
    let delimiter = count + limitItems
    if(pageActual <= totalPage){
        for(let i = count; i < delimiter; i++){
            result.push(items[i])
            count++
        }
    }
    for(let res of result){
        res.style.display = ''
    }
}listItems(getItems(), 1, limitItems)

function getItems(){
    items = []
    for(let id of ids){
        items.push(id)
    }
    return items.splice(1, items.length - 1)
}

function nextPage(){
    hideAllItems()
    pageActual++ 
    listItems(getItems(), pageActual, limitItems)
}
function previousPage(){
    hideAllItems()
    pageActual--
    listItems(getItems(), pageActual, limitItems)
}


let bntNext = document.querySelector('.bnt-next').addEventListener('click', () => nextPage())
let bntPrevious = document.querySelector('.bnt-previous').addEventListener('click', () => previousPage())