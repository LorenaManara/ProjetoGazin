'use strict'

$(document).ready(function(){
    $("#formDesenvolvedores").submit(function(e){
        e.preventDefauld()

        var formulario = new FormData(this)

        $.jax({
            url: "http://localhost:8000/api/Desenvolvedores",
            type: `POST`,
            data: formulario,
            sucess: function(data){
                //exibe uma menssagem de sucesso  e limpa os campos do fornulario
                alert("Desenvolvedor criado com sucesso");
                $(`#formDesenvolvedores`)[0].reset();
            },
            catch: false,
            contentType: false,
            processData: false
        });
    })
})

const openModalDesenvolvedores = () => document.getElementById('modalDesenvolvedores')
    .classList.add('active')

const openModalNiveis = () => document.getElementById('modalNiveis')
    .classList.add('active')

const closeModalDesenvolvedores = () => {
    clearFieldsDesenvolvedores()
    document.getElementById('modalDesenvolvedores').classList.remove('active')
}

const closeModalNiveis = () => {
    clearFieldsNiveis()
    document.getElementById('modalNiveis').classList.remove('active')
}


const getLocalStorage = () => JSON.parse(localStorage.getItem('db_desenvolvedores')) ?? []
const setLocalStorage = (dbdesenvolvedores) => localStorage.setItem("db_desenvolvedores", JSON.stringify(dbdesenvolvedores))

// CRUD - create read update delete
const deleteDesenvolvedores = (index) => {
    const dbDesenvolvedores = readDesenvolvedores()
    dbDesenvolvedores.splice(index, 1)
    setLocalStorage(dbDesenvolvedores)
}

const updateDesenvolvedores = (index, desenvolvedores) => {
    const dbDesenvolvedores = readDesenvolvedores()
    dbDesenvolvedores[index] = desenvolvedores
    setLocalStorage(dbDesenvolvedores)
}

const readDesenvolvedores = () => getLocalStorage()

const createDesenvolvedores = (desenvolvedores) => {
    const dbDesenvolvedores = getLocalStorage()
    dbDesenvolvedores.push (desenvolvedores)
    setLocalStorage(dbDesenvolvedores)
}

const isValidFields = () => {
    return document.getElementById('form').reportValidity()
}

//Interação com o layout

const clearFieldsDesenvolvedores = () => {
    const fields = document.querySelectorAll('.modal-field')
    fields.forEach(field => field.value = "")
}

const clearFieldsNiveis = () => {
    const fields = document.querySelectorAll('.modal-field')
    fields.forEach(field => field.value = "")
}

const saveDesenvolvedores = () => {
    if (isValidFields()) {
        const desenvolvedores = {
            id: document.getElementById('id').value,
            idNivel: document.getElementById('idNivel').value,
            nome: document.getElementById('nome').value,
            DataNascimento: document.getElementById('Data de nascimento').value,
            idade: document.getElementById('idade').value,
            hobby: document.getElementById('hobby').value,
        }
        const index = document.getElementById('nome').dataset.index
        if (index == 'new') {
            createDesenvolvedores(desenvolvedores)
            updateTable()
            closeModal()
        } else {
            updateDesenvolvedores(index, desenvolvedores)
            updateTable()
            closeModal()
        }
    }
}

const createRow = (desenvolvedores, index) => {
    const newRow = document.createElement('tr')
    newRow.innerHTML = `
        <td>${desenvolvedores.id}</td>
        <td>${desenvolvedores.idNivel}</td>
        <td>${desenvolvedores.nome}</td>
        <td>${desenvolvedores.DataNascimento}</td>
        <td>${desenvolvedores.idade}</td>
        <td>${desenvolvedores.hobby}</td>
        <td>
            <button type="button" class="button green" id="edit-${index}">Editar</button>
            <button type="button" class="button red" id="delete-${index}" >Excluir</button>
        </td>
    `
    document.querySelector('#tableDesenvolvedores>tbody').appendChild(newRow)
}

const clearTable = () => {
    const rows = document.querySelectorAll('#tableDesenvolvedores>tbody tr')
    rows.forEach(row => row.parentNode.removeChild(row))
}

const updateTable = () => {
    const dbDesenvolvedores = readDesenvolvedores()
    clearTable()
    dbDesenvolvedores.forEach(createRow)
}

const fillFields = (desenvolvedores) => {
    document.getElementById('id').value = desenvolvedores.id
    document.getElementById('idNivel').value = desenvolvedores.idNivel
    document.getElementById('nome').value = desenvolvedores.nome
    document.getElementById('hobby').value = desenvolvedores.hobby
    document.getElementById('idade').value = desenvolvedores.index.idade
    document.getElementById('DataNascimento').dataset.index = desenvolvedores.DataNascimento
}

const editDesenvolvedores = (index) => {
    const desenvolvedores = readDesenvolvedores()[index]
    desenvolvedores.index = index
    fillFields(desenvolvedores)
    document.querySelector(".modal-header>h2").textContent  = `Editando ${desenvolvedores.nome}`
    openModal()
}

const editDelete = (event) => {
    if (event.target.type == 'button') {

        const [action, index] = event.target.id.split('-')

        if (action == 'edit') {
            editDesenvolvedores(index)
        } else {
            const desenvolvedores = readDesenvolvedores()[index]
            const response = confirm(`Deseja realmente excluir o desenvolvedorese ${desenvolvedores.nome}`)
            if (response) {
                deleteDesenvolvedores(index)
                updateTable()
            }
        }
    }
}

updateTable()

// Eventos
document.getElementById('cadastrarDesenvolvedorese')
    .addEventListener('click', openModalDesenvolvedores)

document.getElementById('cadastrarNiveis')
    .addEventListener('click', openModalNiveis)
    
document.getElementById('modalCloseDesenvolvedores')
    .addEventListener('click', closeModalDesenvolvedores)

document.getElementById('modalCloseNiveis')
    .addEventListener('click', closeModalNiveis)

document.getElementById('salvarDesenvolvedores')
    .addEventListener('click', saveDesenvolvedores)

    //falta salvar Niveis

document.getElementById('cancelarDesenvolvedores')
    .addEventListener('click', closeModalDesenvolvedores)

document.getElementById('cancelarNiveis')
    .addEventListener('click', closeModalNiveis)