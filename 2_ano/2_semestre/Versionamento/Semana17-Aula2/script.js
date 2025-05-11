// Array para armazenar os clientes
let clientes = [];

let usernameRef = document.getElementById("username");
let emailRef = document.getElementById("email");
let eyeL = document.querySelector(".eyeball-l");
let eyeR = document.querySelector(".eyeball-r");
let handL = document.querySelector(".hand-l");
let handR = document.querySelector(".hand-r");

let normalEyeStyle = () => {
  eyeL.style.cssText = `
    left:0.6em;
    top: 0.6em;
  `;
  eyeR.style.cssText = `
  right:0.6em;
  top:0.6em;
  `;
};

let normalHandStyle = () => {
  handL.style.cssText = `
        height: 2.81em;
        top:8.4em;
        left:7.5em;
        transform: rotate(0deg);
    `;
  handR.style.cssText = `
        height: 2.81em;
        top: 8.4em;
        right: 7.5em;
        transform: rotate(0deg)
    `;
};
//When clicked on username input
usernameRef.addEventListener("focus", () => {
  eyeL.style.cssText = `
    left: 0.75em;
    top: 1.12em;  
  `;
  eyeR.style.cssText = `
    right: 0.75em;
    top: 1.12em;
  `;
  normalHandStyle();
});
//When clicked on password input
emailRef.addEventListener("focus", () => {
  handL.style.cssText = `
        height: 6.56em;
        top: 3.87em;
        left: 11.75em;
        transform: rotate(-155deg);    
    `;
  handR.style.cssText = `
    height: 6.56em;
    top: 3.87em;
    right: 11.75em;
    transform: rotate(155deg);
  `;
  normalEyeStyle();
});
//When clicked outside username and password input
document.addEventListener("click", (e) => {
  let clickedElem = e.target;
  if (clickedElem != usernameRef && clickedElem != email) {
    normalEyeStyle();
    normalHandStyle();
  }
});

// Função para adicionar cliente
function adicionarCliente(username, email) {
    const cliente = { username, email };
    clientes.push(cliente);
    exibirClientes();
}

// Função para exibir os clientes na lista
function exibirClientes() {
    const listaClientes = document.getElementById('listaClientes');
    listaClientes.innerHTML = '';

    clientes.forEach((cliente, index) => {
        const li = document.createElement('li');
        li.textContent = `Nome: ${cliente.username}, Email: ${cliente.email}`;
        listaClientes.appendChild(li);
    });
}

// Evento de submissão do formulário
document.getElementById('clienteForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const nome = document.getElementById('username').value;
    const email = document.getElementById('email').value;

    adicionarCliente(nome, email);

    document.getElementById('clienteForm').reset();
});
