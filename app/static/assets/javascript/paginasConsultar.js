class Lista{
    constructor(){
        this.ids = document.querySelectorAll('tr')
        this.qttNextPage = 10
        this.activeItems = 0
        this.currentPage = 0
    }
    get getItems(){
        let listaItems = new Array()
        for(let tr of this.ids){
            listaItems.push(tr)
        }
        return listaItems.splice(1, listaItems.length-1)
    }
    hideAllItems(specificItemsArray = null){
        if(specificItemsArray !== null){
            for(let i of specificItemsArray){
                i.style.display = 'none'
            }
        }else{
            for (let item of this.getItems){
                item.style.display = 'none'
            }
        }
    }
    showItemsByQuantity(quantity = this.qttNextPage){
        if(quantity > this.getItems.length) return 'Máximo Excedido'
        for(let i = 0; i < quantity; i++){
            this.getItems[i].style.display=''
            this.activeItems++
        }
        if(this.currentPage === 0) this.currentPage = 1
    }
    nextPage(){
        this.currentPage++
        let nextPage = this.getItems.splice(this.activeItems, this.qttNextPage)
        this.hideAllItems()
        for(let item of nextPage){
            item.style.display=''
            this.activeItems++
        }
        console.log(this.activeItems, this.getItems.length, this.currentPage, nextPage);
    }
    previousPage(){
        if(this.currentPage > 1) this.currentPage--
        let previousPage = this.getItems.splice(-this.activeItems, this.qttNextPage)
        this.hideAllItems()
        for(let item of previousPage){
            item.style.display=''
            this.activeItems--
        }
        console.log(this.activeItems, this.getItems.length, this.currentPage, previousPage);
    }
}
let lista = new Lista()
lista.hideAllItems()
lista.showItemsByQuantity()

let bntNext = document.querySelector('.bnt-next').addEventListener('click', () => lista.nextPage())
let bntPrevious = document.querySelector('.bnt-previous').addEventListener('click', () => lista.previousPage())