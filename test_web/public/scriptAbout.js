const rating = document.querySelector('#rating');
const names = document.querySelector('#names');
const yearMan = document.querySelector('#year');
const vis = document.querySelector('#vis');

let buttons = [];
let yearsButtons = [];

let yearSelected = 2024;


// Adicionar texto ao corpo
function carregarArquivoMarkdown(arquivo) {
    fetch(arquivo)
        .then(response => response.text())
        .then(text => {
            // Converter o texto Markdown para HTML
            const converter = new showdown.Converter();
            const html = converter.makeHtml(text);

            // Inserir o HTML convertido no elemento de conteúdo
            const divMarkdown = document.getElementById('vis');
            divMarkdown.innerHTML = html;
    }).catch(error => {
        console.error('Erro ao carregar o arquivo Markdown:', error);
    });
}


// Cria o botão
let button = document.createElement('button');

// Define o texto do botão
button.textContent = 'Compare players evolutions';

// Define o evento de clique do botão
button.onclick = function() {
window.location.href = '/search';
};
// Adiciona o botão ao cabeçalho
let header = document.querySelector('header'); // Substitua 'header' pelo seletor correto do seu cabeçalho
header.appendChild(button);

let button2 = document.createElement('button');

// Define o texto do botão
button2.textContent = 'Competitions summary';

// Define o evento de clique do botão
button2.onclick = function() {
window.location.href = '/summary';
};

header.appendChild(button2);

// Cria o botão
let button3 = document.createElement('button');

// Define o texto do botão
button3.textContent = 'About';

// Define o evento de clique do botão
button3.onclick = function() {
window.location.href = '/about';
};

header.appendChild(button3);


const h1 = document.querySelector('h1');

h1.addEventListener('click', () => {
window.location.href = '/';
});


var markdownContent = carregarArquivoMarkdown('texts/about_us.md');


var markdownContainer = document.getElementById('vis');
markdownContainer.innerHTML = marked(markdownContent);
