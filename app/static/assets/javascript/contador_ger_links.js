window.onload = () => {

    let contar = () => {
        let contador = document.querySelector('div#contador')

        let box = document.querySelectorAll('div.activeRes').length
        contador.innerHTML=` 
            <h1>${box}</h1>
        `
        if (document.getElementById('searchbar').value == "" && box == 0){
            let box2 = document.querySelectorAll('div.box').length
            contador.innerHTML=` 
                <h1>${box2}</h1>
            `
        }
        console.log(box, typeof(box))
    }
    contar()
    
    let searchbar = document.getElementById('searchbar').addEventListener('keyup', () => {
        contar()
    })

}
    