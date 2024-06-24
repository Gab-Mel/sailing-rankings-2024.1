const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');
const app = express();
const port = 3000;


let db = new sqlite3.Database('./elo_ranking.db', sqlite3.OPEN_READONLY, (err) => {
  if (err) {
    console.error(err.message);
  }
  console.log('Conectado ao banco de dados SQLite.');
});

let dbPlayers = new sqlite3.Database('./players.db', sqlite3.OPEN_READONLY, (err) => {
  if (err) {
    console.error(err.message);
  }
  console.log('players.db conectado.');
});

let dbSumulas = new sqlite3.Database('./sumulas_simples.db', sqlite3.OPEN_READONLY, (err) => {
  if (err) {
    console.error(err.message);
  }
  console.log('sumulas_simples.db conectado.');
});


dbPlayers.all("SELECT name FROM sqlite_master WHERE type='table';", [], (err, tables) => {
  if (err) {
    throw err;
  }
  tables.forEach((table) => {
    console.log(table.name);
  });
});


db.all("SELECT name FROM sqlite_master WHERE type='table';", [], (err, tables) => {
  if (err) {
    throw err;
  }
  tables.forEach((table) => {
    console.log(table.name);
  });
});

app.get('/sumulas', (req, res) => {
  dbSumulas.all("SELECT name FROM sqlite_master WHERE type='table';", [], (err, tables) => {
    if (err) {
      throw err;
    }
    tablesNames = tables.map(table => table.name);
    res.send(tablesNames);
  });
});

app.get('/tables', (req, res) => {
  db.all("SELECT name FROM sqlite_master WHERE type='table';", [], (err, tables) => {

    tablesNames = tables.map(table => table.name);
    res.send(tablesNames);
  });
});

app.get('/year', (req, res) => {
  const table = req.query.table;
  db.all(`SELECT DISTINCT Year FROM '${table}' ORDER BY Year DESC`, [], (err, rows) => {
    if (err) {
      throw err;
    }
    res.send(rows);
  });
});

app.get('/rating', (req, res) => {
  const table = req.query.table;
  const year = req.query.year;
  db.all(`SELECT * FROM '${table}' WHERE Year = ${year}`, [], (err, rows) => {
    if (err) {
      throw err;
    }
    res.send(rows);
  });
})

app.get('/sumulasT', (req, res) => {
  const table = req.query.table;
  dbSumulas.all(`SELECT * FROM '${table}';`, [], (err, rows) => {
    if (err) {
      throw err;
    }
    res.send(rows);
  });
})

var table;

// Rota para puxar todos os dados de uma tabela específica
app.get('/data', (req, res) => {
  table = req.query.table;
  db.all(`SELECT DISTINCT "index" FROM '${table}'`, (err, rows) => {
    if (err) {
      throw err;
    }
    res.send(rows);
  });
});

app.get('/query', (req, res) => {
  const data = JSON.parse(req.query.data);
  const placeholders = data.map(() => '?').join(',');
  const sqlRating = `
  WITH RankedAthletes AS (
    SELECT "index", "Rating", "Year", 
           RANK() OVER (PARTITION BY "Year" ORDER BY "Rating" DESC) AS Position
    FROM '${table}'
  )
  SELECT * FROM RankedAthletes
  WHERE "index" IN (${placeholders})
  ORDER BY "Year", "Rating" DESC;
  `;
  db.all(sqlRating, data, (err, rows) => {
    if (err) {
      throw err;
    }
    res.send(rows);
  });
});

app.get('/queryplayer', (req, res) => {
  const data = JSON.parse(req.query.data);
  const placeholders = data.map(() => '?').join(',');
  const tables = JSON.parse(req.query.tables);
  const queries = tables.map((table) => {
    return new Promise((resolve, reject) => {
      const sqlRating = `
      WITH RankedAthletes AS (
        SELECT "index", "Rating", "Year", 
               RANK() OVER (PARTITION BY "Year" ORDER BY "Rating" DESC) AS Position
        FROM '${table}'
      )
      SELECT * FROM RankedAthletes
      WHERE "index" IN (${placeholders})
      ORDER BY "Year", "Rating" DESC;
      `;
      db.all(sqlRating, data, (err, rows) => {
        if (err) {
          reject(err);
        } else {
          // Use o nome da tabela como chave e os resultados como valor
          resolve({[table]: rows});
        }
      });
    });
  });

  Promise.all(queries)
    .then(results => {
      // Combine todos os objetos de resultados em um único objeto
      const combinedResults = results.reduce((acc, current) => {
        return {...acc, ...current};
      }, {});
      res.json(combinedResults); // Envie o objeto combinado como JSON
    })
    .catch(error => {
      console.error("Erro ao processar consultas:", error);
      res.status(500).send("Erro ao processar consultas");
    });
});

// cria uma rota '/' que retorna a pasta public

app.use(express.static('public'));

// Rota para a página inicial
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Rota para outra página
app.get('/search', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'search.html'));
});

//Rota para a página players
app.get('/players', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'players.html'));
});

app.get('/summary', (req, res) =>{
  res.sendFile(path.join(__dirname, 'public', 'summary.html'));
})

app.get('/playersapi', (req, res) => {
  const name = req.query.name;
  dbPlayers.all(`SELECT * FROM "Resultados" WHERE "Nome" = "${name}"`, [], (err, rows) => {
    if (err) {
      throw err;
    }
    res.send(rows);
  });
});

app.listen(port, () => {
  console.log(`Servidor rodando em http://localhost:${port}`);
});
