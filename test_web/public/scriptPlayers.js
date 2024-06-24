const urlParams = new URLSearchParams(window.location.search);
const playerName = urlParams.get('name');
const rating = document.getElementById('rating');

console.log(playerName);
let uniqueClasses = new Set();

function getMinMaxBound(data){
    let min = data[0].Rating;
    let max = data[0].Rating;
    data.forEach(row => {
      if (row.Rating < min) {
        min = row.Rating;
      }
      if (row.Rating > max) {
        max = row.Rating;
      }
    });
    return [min-50, max+50];
}

fetch(`/playersapi?name=${playerName}`).then(response => response.json()).then(data => {
    console.log(data);
    let cSport = '';
    let country;
    let name = playerName;
    var bestRating = 1000;
    data.forEach(item => {
        uniqueClasses.add(item.Classe);
        if(country === undefined && item['Nacionalidade'] !== undefined) {
            country = item['Nacionalidade'];
        };
        if(item['Colocação'] < bestRating) {
            bestRating = item['Colocação'];
        }
    });

    if(country === undefined) {
        country = 'unknown country';
    }

    console.log(bestRating)

    // get all competitions with best rating

    const competitions = [];
    
    data.forEach(item => {
        if(item['Colocação'] === bestRating) {
            competitions.push(item);
        }
    });

    uniqueClasses = Array.from(uniqueClasses);
    
    const text = `The player ${name} of ${country} has the best rating of ${bestRating} in the following competitions: ${competitions.map(item => item['Competição']).join(', ')}. The player has participated in ${uniqueClasses.join(' and ')} class. The first time the player was seen was in ${data[0]['Data da Competição']}.`

    document.getElementById('player').textContent = text;

    const queryString = JSON.stringify([playerName]);
    const uniqueClassesJSON = JSON.stringify(uniqueClasses);
    console.log(uniqueClassesJSON);

    rating.innerHTML = '';
        
    // Cria a tabela e adiciona cabeçalho
    const table = document.createElement('table');
    const thead = document.createElement('thead');
    const tbody = document.createElement('tbody');
    const headerRow = document.createElement('tr');
    
    ['Name', 'Position', 'Competition','Year','Class'].forEach(text => {
        const th = document.createElement('th');
        th.appendChild(document.createTextNode(text));
        headerRow.appendChild(th);
    });
    
    thead.appendChild(headerRow);
    table.appendChild(thead);
    
    // Adiciona os dados à tabela
    data.forEach((item, i) => {
        const row = document.createElement('tr');
        
        [item['Nome'],item["Colocação"],item["Competição"],item["Data da Competição"],item["Classe"]].forEach(text => {
            const td = document.createElement('td');
            td.appendChild(document.createTextNode(text));
            row.appendChild(td);
        });
        
        tbody.appendChild(row);
    });
    
    table.appendChild(tbody);
    rating.appendChild(table);

    return fetch(`/queryplayer?data=${queryString}&tables=${uniqueClassesJSON}`)
    .then(response => response.json())
    .then(data => {
    console.log(data);
    data = Object.entries(data).flatMap(([tableName, rows]) =>
        rows.map(row => ({ ...row, Year: new Date(row.Year, 0), Table: tableName }))
      );
    //   minMaxBound = getMinMaxBound(transformedData);
      console.log(data);
    var yourVlSpec = {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "description": "Gráfico de linhas mostrando Rating por Year, com linhas coloridas por Table.",
        "data": {
          "values": data
        },
        "width": 500,
        "height": 270,
        title: `${playerName} Elo Rating Evolution`,
        "mark": "line",
        "encoding": {
          "x": {
            "field": "Year",
            "type": "temporal",
            "axis": {"title": "Ano"}
          },
          "y": {
            "field": "Rating",
            "type": "quantitative",
            "axis": {"title": "Rating"}
          },
          "color": {
            "field": "Table",
            "type": "nominal",
            "legend": {"title": "Class"}
          }
        },
      }

    vegaEmbed('#vis', yourVlSpec);
    var yourVlSpec2 = {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "description": "Gráfico de linhas mostrando Rating por Year, com linhas coloridas por Table.",
        "data": {
          "values": data
        },
        "width": 500,
        "height": 270,
        title: `${playerName} Elo Classification Evolution`,
        "mark": "line",
        "encoding": {
          "x": {
            "field": "Year",
            "type": "temporal",
            "axis": {"title": "Ano"}
          },
          "y": {
            "field": "Position",
            "type": "quantitative",
            "axis": {"title": "Position"},
            "scale": {"reverse": true}
          },
          "color": {
            "field": "Table",
            "type": "nominal",
            "legend": {"title": "Class"}
          }
        },
      }
    vegaEmbed('#vis2', yourVlSpec2);

})


}).catch(error => console.error("Falha ao buscar dados do jogador:", error));

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


const h1 = document.querySelector('h1');

h1.addEventListener('click', () => {
  window.location.href = '/';
});
