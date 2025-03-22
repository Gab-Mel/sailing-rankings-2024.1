/*CREATE TABLE athlete (
    id int PRIMARY KEY,
    name TEXT NOT NULL,
    nationality TEXT,
    age INT 
);

CREATE TABLE competition (
    id int PRIMARY KEY,
    name TEXT NOT NULL,
    year INT
);

CREATE TABLE final_data (
    id INT PRIMARY KEY,
    id_atleta INT NOT NULL,
    id_competicao INT NOT NULL,
    classe_vela TEXT NOT NULL,
    pontuacao_regata INT NOT NULL,
    descarte INT NOT NULL,
    flotilha TEXT NOT NULL,
    posicao INT NOT NULL,
    punicao TEXT NOT NULL,
    pontuacao_total FLOAT NOT NULL,
    nett INT NOT NULL,
    FOREIGN KEY (id_atleta) REFERENCES athlete(id),
    FOREIGN KEY (id_competicao) REFERENCES competition(id)
);
*/

CREATE TABLE ranking_elo_40 (
    id_atleta INT NOT NULL,
    score FLOAT NOT NULL,
    class_vela TEXT NOT NULL,
    year INT NOT NULL,
    FOREIGN KEY (id_atleta) REFERENCES athlete(id),
    PRIMARY KEY (id_atleta, class_vela, year)
);

