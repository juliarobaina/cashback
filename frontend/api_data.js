document.addEventListener("DOMContentLoaded", () => {
    historico()     
    cashback()
    mascara_desconto()
    mascara_valor()
})

async function historico(){
    const cashback = await fetch("https://cashback-0j64.onrender.com/historico")
    const cashbackJson = await cashback.json()
    get_historico(cashbackJson)

   
}

function get_historico(cashbackJson){
    let rows = ""
    const table = document.getElementById("history_table")
    cashbackJson.forEach(item => {
        rows += `<tr>
                <td>${item.tipoCliente}</td>
                <td>${Number(Math.trunc(item.valorDescontado * 100) / 100).toLocaleString("pt-BR", { maximumFractionDigits: 2 })}</td>
                <td>${Number(Math.trunc(item.valor * 100) / 100).toLocaleString("pt-BR", { maximumFractionDigits: 2 })}</td>
                <td>${item.desconto}</td>
                <td>${Number(Math.trunc(item.cashback * 100) / 100).toLocaleString("pt-BR", { maximumFractionDigits: 2 })}</td>
            </tr>`
    });

    table.innerHTML = rows
    
    const tableTitle = document.getElementById("tableTitle")
    tableTitle.innerText = "IP " + `${cashbackJson[0].ip}`
}


function cashback(){ 
    const form = document.getElementById("form")
    
    form.addEventListener("submit", async function(event){
        event.preventDefault()

        const data = new FormData(form)

        let obj = Object.fromEntries(data)

        if (obj.valor) {
            obj.valor = obj.valor
                .replace(/\./g, "")   // remove pontos
                .replace(",", ".")    // troca vírgula por ponto
        }

        if(!obj.desconto){
            obj.desconto = 0
        }

        await fetch("https://cashback-0j64.onrender.com/cashback",{
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(obj)
        })
       
        form.reset()
        await historico()

    })
    
   
}


function mascara_desconto() {
    const input = document.getElementById("cupomDesconto")
    
    input.addEventListener("input", function(){
        let valor = input.value
        let id = document.getElementById("msg")
        if (!/^[0-9]*$/.test(valor)) {
            input.value = valor.slice(0, -1)
            return
        }

        if (valor !== "" && parseInt(valor) > 100) {
            id.innerText = "Digite números entre 0 e 100"
        }else{
            id.innerText = ""
        }
    })
}

function mascara_valor() {
    const input = document.getElementById("valorCompra")

    input.addEventListener("input", function () {
        let valor = input.value
        let msg = document.getElementById("msgValor")

        // remove tudo que não for número
        let somenteNumeros = valor.replace(/\D/g, "")

        // limita até 12 digitos
        if (somenteNumeros.length > 12) {
            input.value = valor.slice(0, -1)
            return
        }

        // se tiver letras ou símbolos inválidos
        if (!/^[0-9.,]*$/.test(valor)) {
            input.value = valor.slice(0, -1)
            return
        }

        // formatação progressiva
        let numero = somenteNumeros

        if (numero.length > 2) {
            numero = numero.replace(/(\d)(\d{2})$/, "$1,$2")
        }

        numero = numero.replace(/\B(?=(\d{3})+(?!\d))/g, ".")

        input.value = numero
    })
}