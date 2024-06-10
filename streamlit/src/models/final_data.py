from dataclasses import dataclass
from src.utils.db import db, DB
from src.utils.repository import Repository
from typing import Optional
from uuid import uuid4
from hashlib import sha256

@dataclass
class FinalData:
    id: str
    athlete_id: str
    competition_id: str
    classe_vela: str
    pontuacao_regata: int
    descarte: int
    flotilha: str
    posicao: int
    punicao: str
    pontuacao_total: float
    nett: int

@dataclass
class FinalDataRepository(Repository):
    db: DB
    
    def __init__(self):
        self.db = db
    
    def create(self, **attrs) -> Optional[FinalData]:
        id = str(attrs.get('id'))
        athlete_id = str(attrs.get('athlete_id'))
        competition_id = str(attrs.get('competition_id'))
        classe_vela = str(attrs.get('classe_vela'))
        pontuacao_regata = str(attrs.get('pontuacao_regata'))
        descarte = str(attrs.get('descarte'))
        flotilha = str(attrs.get('flotilha'))
        posicao = str(attrs.get('posicao'))
        punicao = str(attrs.get('punicao'))
        pontuacao_total = str(attrs.get('pontuacao_total'))
        nett = str(attrs.get('nett'))
        
        result = self.db.execute(
            "INSERT INTO final_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (id, athlete_id, competition_id, classe_vela, pontuacao_regata, 
             descarte, flotilha, posicao, punicao, pontuacao_total, nett)
        )
        if result is None:
            return None
        
        if result is not None:
            return self.read(id=id)
        
    def read(self, **attrs) -> Optional[FinalData]:
        wheres = []
        params = tuple()
        
        for key, value in attrs.items():
            wheres.append(f"{key} = ?")
            params = (*params, value)
            
        where = " AND ".join(wheres)
        
        result = self.db.execute(
            f"select * from final_data where {where}",
            params
        )
        
        if (result is None or result == []):
            return None

        return FinalData(*result[0])
    
    def list(self) -> Optional[FinalData]:
        result = self.db.execute("select * from final_data")
        
        if (result is None or result == []):
            return None

        return [FinalData(*row) for row in result]
    
    def update(self, final_data: FinalData, **attrs) -> Optional[FinalData]:
        id = final_data.id
        athlete_id = attrs.get('athlete_id')
        competition_id = attrs.get('competition_id')
        classe_vela = attrs.get('classe_vela')
        pontuacao_regata = attrs.get('pontuacao_regata')
        descarte = attrs.get('descarte')
        flotilha = attrs.get('flotilha')
        posicao = attrs.get('posicao')
        punicao = attrs.get('punicao')
        pontuacao_total = attrs.get('pontuacao_total')
        nett = attrs.get('nett')
        
        result = self.db.execute(
            "UPDATE final_data SET athlete_id = ?, competition_id = ?, classe_vela = ?, pontuacao_regata = ?, descarte = ?, flotilha = ?, posicao = ?, punicao = ?, pontuacao_total = ?, nett = ? WHERE id = ?",
            (athlete_id, competition_id, classe_vela, pontuacao_regata, descarte, flotilha, posicao, punicao, pontuacao_total, nett, id)
        )
        if result is None:
            return None
        
        return self.read(id)
    
    def delete(): ...
    
