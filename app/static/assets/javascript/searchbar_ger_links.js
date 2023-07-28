function pesquisar_item(){
    let input = document.getElementById('searchbar').value;
    input = input.toLowerCase();

    let x = document.getElementsByTagName('h3');

    let y = document.getElementsByClassName('box');

    let z = document.getElementById('aviso'); //NÃO UTILIZADO

    for (i = 0; i < x.length; i++) { 
        if (!x[i].innerHTML.toLowerCase().includes(input)) {
            x[i].style.display="none";
            y[i].style.display='none';
            y[i].classList.remove('activeRes')
        }
        else {
            x[i].style.display="inline";
            y[i].style.display='flex';
            y[i].classList.add('activeRes')
        }
    }
}
let search = document.getElementById('searchbar').addEventListener('keyup', pesquisar_item)