let xml = new XMLHttpRequest()
let norefresh = () => {
    xml.onreadystatechange = () => {
        if(xml.readyState == 4 && xml.status == 200){
            try{
                // document.getElementById('pg-home').innerHTML = xml.responseText
                let inicioCards = xml.responseText.indexOf('id="cards"')
                let finalCards = xml.responseText.indexOf('<!--Final Cards-->')
                response = ''
                for(i=inicioCards; i<=finalCards; i++){
                    response += xml.responseText.trim()
                }
                console.log(response)
                document.getElementById('cards').innerHTML = response
            }catch(error){
                return
            }
        }
    }
    xml.open("GET", '/', true)
    xml.send()
}
// let autoRefresh = setInterval(() => {
//     norefresh()
// }, 300)