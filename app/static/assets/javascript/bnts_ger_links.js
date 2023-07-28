// let bntAdd = document.getElementById('bntAdd').addEventListener('click', function(){
//     let formAdicionar = document.getElementById('formAdicionar').style.display='flex';
//     document.body.style.position='fixed'
// })
// let bntAddClose = document.getElementById('bntCAdicionar').addEventListener('click', function(){
//     let formEd = document.getElementById('formAdicionar').style.display='none';
//     document.body.style.position='static'
// })

// let bntRem = document.getElementById('bntRem').addEventListener('click', function(){
//     let formAdicionar = document.getElementById('formRemover').style.display='flex';
//     document.body.style.position='fixed'
// })
// let bntRemClose = document.getElementById('bntCRemover').addEventListener('click', function(){
//     let formEd = document.getElementById('formRemover').style.display='none';
//     document.body.style.position='static'
// })

let bntRem = document.querySelector('#bnt-rem-ger')

let bntAdd = document.querySelector('#bnt-add-ger')
let formAdd = document.querySelector('#formEd')

bntAdd.addEventListener('click', () => {
    formAdd.classList.add('visivel-form-ger')
})