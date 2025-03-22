from dataclasses import dataclass
from src.utils.db import db, DB
from src.utils.repository import Repository
from typing import Optional
from uuid import uuid4
from hashlib import sha256

@dataclass
class Competition:
    id: str
    name: str
    year: int

@dataclass
class CompetitionRepository(Repository):
    bd: DB

    def __init__(self):
        self.db = db  
        
    def create(self, **attrs) -> Optional[Competition]:
        id = attrs.get('id')
        name = attrs.get('name')
        year = attrs.get('year')
        
        result = self.db.execute(
            "INSERT INTO competition VALUES (?, ?, ?)",
            (str(id), str(name), str(year))
        )
        if result is None:
            return None
        
        if result is not None:
            return self.read(id=id)
        
    def read(self, **attrs) -> Optional[Competition]:
        wheres = []
        params = tuple()
        
        for key, value in attrs.items():
            wheres.append(f"{key} = ?")
            params = (*params, value)
            
        where = " AND ".join(wheres)
        
        result = self.db.execute(
            f"select * from competition where {where}",
            params
        )
        
        if (result is None or result == []):
            return None

        return Competition(*result[0])
    
    def update(self, competition: Competition, **attrs) -> Optional[Competition]:
        id = str(competition.id)
        name = str(attrs.get('name'))
        year = str(attrs.get('year'))
        
        result = self.db.execute(
            "UPDATE competitions SET name = ?, year = ? WHERE id = ?",
            (name, year, id)
        )
        if result is None:
            return None
        
        return self.read(id=id)
    
    def delete(self, competition: Competition) -> Optional[Competition]:
        id = str(competition.id)
        
        result = self.db.execute(
            "DELETE FROM competitions WHERE id = ?",
            (id,)
        )
        if result is None:
            return None
        
        return competition
    
    def list(self) -> Optional[Competition]:
        result = self.db.execute("SELECT * FROM competitions")
        if result is None:
            return None
        
        return [Competition(*r) for r in result]
    
    def delete(): ...
    