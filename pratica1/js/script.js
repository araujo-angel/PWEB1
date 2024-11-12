const usuarios = [];

const listaUsuariosElement = document.createElement('ul');
document.body.appendChild(listaUsuariosElement);

for (let usuario of usuarios) {
    inserirUsuarioNaLista(usuario);
}

function inserirUsuario() {
    const inputNomeElement = document.querySelector('#nome').value;
    const inputIdadeElement = document.querySelector('#idade').value;
    const inputCpfElement = document.querySelector('#cpf').value;
    const usuario = {nome: inputNomeElement, idade: inputIdadeElement, cpf: inputCpfElement}
    inserirUsuarioNaLista(usuario);
}

function inserirUsuarioNaLista(usuario) {
    const liElement = document.createElement('li');
    const botaoRemoverElement = document.createElement('button');
    botaoRemoverElement.textContent = 'X';
    botaoRemoverElement.addEventListener('click', (event) => {
        liElement.remove();
    });

    const spanElement = document.createElement('span');
    spanElement.textContent = `Nome: ${usuario.nome}, Idade: ${usuario.idade}, CPF: ${usuario.cpf} `;

    spanElement.addEventListener('click', event => {
        const inputElement = usuario('input');
        inputElement.value = usuario;
        liElement.appendChild(inputElement);
        spanElement.remove();
    });

    liElement.appendChild(spanElement);
    liElement.appendChild(botaoRemoverElement);

    listaUsuariosElement.appendChild(liElement);
}