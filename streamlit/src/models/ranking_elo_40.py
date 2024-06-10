from dataclasses import dataclass
from src.utils.db import db, DB
from src.utils.repository import Repository
from typing import Optional

@dataclass
class RankingElo40:
    id_atleta: str
    score: float
    class_vela: str
    year: int

@dataclass
class RankingElo40Repository(Repository):
    db: DB
    
    def __init__(self):
        self.db = db
        
    def create(self, **attrs) -> Optional[RankingElo40]:
        id_atleta = str(attrs.get('id_atleta'))
        score = str(attrs.get('score'))
        class_vela = str(attrs.get('class_vela'))
        year = str(attrs.get('year'))
        
        result = self.db.execute(
            "INSERT INTO ranking_elo_40 VALUES (?, ?, ?, ?)",
            (id_atleta, score, class_vela, year)
        )
        if result is None:
            return None
        
        if result is not None:
            return self.read(id_atleta = id_atleta, class_vela = class_vela, year = year)
        
    def read(self, **attrs) -> Optional[RankingElo40]:
        wheres = []
        params = tuple()
        
        for key, value in attrs.items():
            wheres.append(f"{key} = ?")
            params = (*params, value)
            
        where = " AND ".join(wheres)
        
        result = self.db.execute(
            f"select * from ranking_elo_40 where {where}",
            params
        )
        
        if (result is None or result == []):
            return None

        return RankingElo40(*result[0])
    
    def update(self, ranking_elo_40: RankingElo40, **attrs) -> Optional[RankingElo40]:
        id_atleta = ranking_elo_40.id_atleta
        score = attrs.get('score')
        class_vela = attrs.get('class_vela')
        year = attrs.get('year')
        
        result = self.db.execute(
            "UPDATE ranking_elo_40 SET score = ?  WHERE class_vela = ? AND year = ? AND id_atleta = ? ",
            (score, class_vela, year, id_atleta)
        )
        if result is None:
            return None
        
        return self.read(id_atleta)
    
    def list(self, year, class_vela) -> Optional[RankingElo40]:
        result = self.db.execute("select * from ranking_elo_40 where class_vela = ? AND year = ?", (class_vela, year,))
        #result = self.db.execute("select * from ranking_elo_40")
        
        if (result is None or result == []):
            print('result is none')
            return None

        return result
    
    def list_by_athletes(self, year, class_vela, atletas) -> Optional[RankingElo40]:
        """
        atletas = str(atletas)
        atletas = atletas.replace("\'", "'")
        atletas = atletas.replace("('", "'")
        atletas = atletas.replace("')", "'")
        atletas = atletas.replace("',)", "'")
        atletas = atletas.replace("'", "")
        """
        print(atletas)
        lista = []
        lista.append(class_vela)
        for i in range(len(atletas)):
            lista.append(atletas[i])
            
        tupla = tuple(lista)
        
        print(tupla)
        if len(atletas) == 1:
            result = self.db.execute("select * from ranking_elo_40 where class_vela = ? AND id_atleta = ?", tupla)
        else:
            result = self.db.execute(f"select * from ranking_elo_40 where class_vela = ? AND id_atleta IN (?{',?'*(len(atletas)-1)})", tupla)
        
        if (result is None or result == []):
            print('result is none')
            return None

        return result
    
    def list_atleta(self, atleta) -> Optional[RankingElo40]:
        result = self.db.execute("select * from ranking_elo_40 where id_atleta = ?", (atleta,))
        #result = self.db.execute("select * from ranking_elo_40")
        
        if (result is None or result == []):
            print('result is none')
            return None

        return result
    
    
    def delete(): ...
    