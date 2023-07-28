let semOrdens = document.getElementById('semOrdens')
let cards = document.querySelectorAll(".card")
let body = document.querySelector('body')

let bntVoltarMobile = document.getElementById('bnt-voltar-img').addEventListener('click', () =>{
    window.history.back() //BOTÃO DE VOLTAR
})

if (cards.length === 0){ //MOSTRAR 'SEM ORDENS' QUANDO NÃO TIVER ORDENS
    semOrdens.style.display='block'
}

//VERFICAÇÃO CONTÍNUA DO BANCO DE DADOS E SOLICITAR ATUALIZAÇÃO DA PÁGINA AO DETECTAR ALTERAÇÕES
//COMPARAR O PRIMEIRO PEDIDO DE JSON COM O SEGUNDO PEDIDO DE JSON, E REPETIR O CICLO
//ARMAZENAS EM UMA VARIÁVEL GLOBAL WINDOW.ONLOAD
// let car = fetch("/ordens-list", {
//   method: "POST",
//   headers: {
//     "Content-Type": "application/json",
//   },
// //   body: JSON.stringify(data),
// })
//   .then((response) => response.json())
//   .then((data) => {
//     return data;
//   })
//   .catch((error) => {
//     console.error("Error:", error);
//   });

// console.log(car);