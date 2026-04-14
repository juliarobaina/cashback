document.addEventListener("DOMContentLoaded", () => {
    cashback()     
    cashback2()
})

async function cashback(){
    const cashback = await fetch("http://127.0.0.1:8000/historico")
    const cashbackJson = await cashback.json()
    j(cashbackJson)

   
}

function j(cashbackJson){
 let rows = ""
    const table = document.getElementById("history_table")
    cashbackJson.forEach(item => {
        rows += `<tr>
                <td>${item.tipoCliente}</td>
                <td>${item.valor}</td>
                <td>${item.cashback}</td>
            </tr>`
    });

    table.innerHTML = rows
    
    const tableTitle = document.getElementById("tableTitle")
    tableTitle.innerText = "IP " + `${cashbackJson[0].ip}`
}


function cashback2(){ 
    const form = document.getElementById("form")
    
    form.addEventListener("submit", async function(event){
        event.preventDefault()

        const data = new FormData(form)
   
        await fetch("http://127.0.0.1:8000/cashback",{
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(Object.fromEntries(data))
        })
       
        form.reset()
        await cashback()

    })
    
   
}