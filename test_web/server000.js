"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var express_1 = require("express");
var sqlite3_1 = require("sqlite3");
var app = (0, express_1.default)();
var port = 3000;
// Cria uma nova instância do banco de dados SQLite
var db = new sqlite3_1.default.Database('./elo_ranking.db', sqlite3_1.default.OPEN_READONLY, function (err) {
    if (err) {
        console.error(err.message);
    }
    console.log('Conectado ao banco de dados SQLite.');
});
// Rota para puxar todos os dados de uma tabela específica
app.get('/data', function (req, res) {
    db.all("SELECT * FROM nome_da_tabela", function (err, rows) {
        if (err) {
            throw err;
        }
        res.send(rows);
    });
});
app.listen(port, function () {
    console.log("Servidor rodando em http://localhost:".concat(port));
});
