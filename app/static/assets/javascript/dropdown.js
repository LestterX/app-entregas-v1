/*
ATIVA E DESATIVA O display:block NO dropdown-content QUANDO PRESSIONA o bnt-menu-img
*/
let dropdown = document.getElementById("dropdown-content")

let bntMobile = document.getElementById('bnt-menu-img').addEventListener('click', () => {
    dropdown.classList.toggle('show')
    if(dropdown.classList[0] === 'show'){
        dropdown.style.display = 'block'
    }else{
        dropdown.style.display = 'none'
    }

})
window.onclick = function(event) {
    if (!event.target.matches('#bnt-menu-img')) {
      dropdown.style.display='none'
      dropdown.classList.remove('show')
    }
}