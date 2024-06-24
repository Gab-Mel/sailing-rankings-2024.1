const rating = document.querySelector('#rating');
const names = document.querySelector('#names');
const yearMan = document.querySelector('#year');

let buttons = [];
let yearsButtons = [];

let yearSelected = 2024;


fetch('/tables').then(response => response.json()).then(data => {
  console.log(data);
  data.forEach(table => {
    fetch('/year?table='+table).then(response => response.json()).then(data => {
      console.log(data);
      const years = data; // Agora 'years' é um array de anos
      const yearsDiv = document.createElement('select');
      yearsDiv.classList.add('yearsDiv');
      // display: none;
      yearsDiv.style.display = 'none';
    
      // Adiciona cada ano como uma opção no select
      let maxYear = 0;
      years.forEach(year => {
        year = year.Year;
        if (year > maxYear) {
          maxYear = year;
        }
        const option = document.createElement('option');
        option.value = year;
        option.textContent = year;
        yearsDiv.appendChild(option);
      });

    
      // Adiciona o select ao documento
      names.appendChild(yearsDiv);
    
      // Adiciona um ouvinte de eventos para atualizar 'years' com base na seleção
      yearsDiv.addEventListener('change', function() {
        yearSelected = this.value;
        fetch(`/rating?table=${table}&year=${yearSelected}`).then(response => response.json()).then(data => {
          rating.innerHTML = '';
          
          // Cria a tabela e adiciona cabeçalho
          const table = document.createElement('table');
          const thead = document.createElement('thead');
          const tbody = document.createElement('tbody');
          const headerRow = document.createElement('tr');
          
          ['Position', 'Name', 'Rating'].forEach(text => {
              const th = document.createElement('th');
              th.appendChild(document.createTextNode(text));
              headerRow.appendChild(th);
          });
          
          thead.appendChild(headerRow);
          table.appendChild(thead);
          
          // Adiciona os dados à tabela
          data.forEach((item, i) => {
              const row = document.createElement('tr');
              
              // [i+1, item.index, Number(item.Rating).toFixed(2)].forEach(text => {
              //     const td = document.createElement('td');
              //     td.appendChild(document.createTextNode(text));
              //     row.appendChild(td);
              // });
              [i+1, item.index, Number(item.Rating).toFixed(2)].forEach(text => {
                if (text === item.index) {
                    const button = document.createElement('button');
                    button.textContent = 'Go to Google';
                    button.onclick = function() {
                        window.location.href = 'https://www.google.com/search?q=' + encodeURIComponent(item.index);
                    };
                    const td = document.createElement('td');
                    td.appendChild(button);
                    row.appendChild(td);
                } else {
                    const td = document.createElement('td');
                    td.appendChild(document.createTextNode(text));
                    row.appendChild(td);
                }
            });

              row.addEventListener('click', () => {
                window.location.href = "https://google.com" //`/player?table=${table}&year=${yearSelected}&index=${item.index}`;
              });
              
              tbody.appendChild(row);
          });
          
          table.appendChild(tbody);
          rating.appendChild(table);
        });
      });

      yearSelected = maxYear;

      yearsButtons.push(yearsDiv);
    
    }).catch(error => console.error("Falha ao buscar anos:", error));
    const b = document.createElement('button');
    buttons.push(b);
    b.addEventListener('click', () => {
      // change the button color to #ededed and the others to white
      buttons.forEach(button => {
        button.style.backgroundColor = '#3d71a2';
        button.style.color = 'white';
      });
      b.style.backgroundColor = '#012B39';
      b.style.color = '#E2B842';

      // obter o índice de 'b' em 'buttons'
      const index = buttons.indexOf(b);

      // obter o ano selecionado
      yearSelected = yearsButtons[index].value;

      // modificar o display de none para block

      yearsButtons.forEach(yearsDiv => {
        yearsDiv.style.display = 'none';
      });

      yearsButtons[index].style.display = 'flex';
      
      console.log(yearSelected);
      fetch(`/rating?table=${table}&year=${yearSelected}`).then(response => response.json()).then(data => {
        rating.innerHTML = '';
        
        // Cria a tabela e adiciona cabeçalho
        const table = document.createElement('table');
        const thead = document.createElement('thead');
        const tbody = document.createElement('tbody');
        const headerRow = document.createElement('tr');
        
        ['Position', 'Name', 'Rating'].forEach(text => {
            const th = document.createElement('th');
            th.appendChild(document.createTextNode(text));
            headerRow.appendChild(th);
        });
        
        thead.appendChild(headerRow);
        table.appendChild(thead);
        
        // Adiciona os dados à tabela
        data.forEach((item, i) => {
            const row = document.createElement('tr');
            
            // [i+1, item.index, Number(item.Rating).toFixed(2)].forEach(text => {
            //     const td = document.createElement('td');
            //     td.appendChild(document.createTextNode(text));
            //     row.appendChild(td);
            // });
            [i+1, item.index, Number(item.Rating).toFixed(2)].forEach((text, columnIndex) => {
              const td = document.createElement('td');
              td.appendChild(document.createTextNode(text));
              row.appendChild(td);
      
              // Verifica se a coluna atual é a do nome do atleta
              if (columnIndex === 1) {
                  // Supondo que a URL possa ser construída assim
                  const athleteUrl = `players.html?name=${encodeURIComponent(item.index)}`;
                  td.setAttribute('data-url', athleteUrl);
                  td.style.cursor = 'pointer'; // Muda o cursor para indicar clicabilidade
                  td.addEventListener('click', function() {
                      window.location.href = this.getAttribute('data-url');
                  });
              }
          });
            
            tbody.appendChild(row);
        });
        
        table.appendChild(tbody);
        rating.appendChild(table);
      });
    });
    const t = document.createTextNode(table);
    b.appendChild(t);
    names.appendChild(b);
  });
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
