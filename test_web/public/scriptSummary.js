names = document.querySelector('#names');
rating = document.querySelector('#rating');
fetch('/sumulas').then(response => response.json()).then(data => {
    console.log(data);
    const divS = document.createElement('select');
    divS.classList.add('divS');
    data.forEach(s => {
        const option = document.createElement('option'); // Correção: criar a option dentro do loop
        option.value = s;
        option.textContent = s;
        divS.appendChild(option);
    });
    names.appendChild(divS);

    // Função para carregar os dados com base no valor selecionado
    const loadData = (value) => {
        fetch(`/sumulasT?table=${value}`).then(response => response.json()).then(data => {
            rating.innerHTML = '';
            const table = document.createElement('table');
            const thead = document.createElement('thead');
            const tbody = document.createElement('tbody');
            const headerRow = document.createElement('tr');
            ['Position', 'Name', "Nett", 'Total', 'Country'].forEach(text => {
                const th = document.createElement('th');
                th.appendChild(document.createTextNode(text));
                headerRow.appendChild(th);
            });
            thead.appendChild(headerRow);
            table.appendChild(thead);
            data.forEach(row => {
                const tr = document.createElement('tr');
                ['Posição', 'Nome Competidor', 'Nett', 'Total', 'Nacionalidade'].forEach(column => {
                    const td = document.createElement('td');
                    td.appendChild(document.createTextNode(row[column]));
                    tr.appendChild(td);
                });
                tbody.appendChild(tr);
            });
            table.appendChild(tbody);
            rating.appendChild(table);
        });
    };

    // Adiciona o evento de mudança ao select
    divS.addEventListener('change', function () {
        loadData(this.value);
    });

    // Executa a função loadData com o valor padrão do select assim que as opções são adicionadas
    loadData(divS.value);
});

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
