from dataclasses import dataclass
from src.utils.db import db, DB
from src.utils.repository import Repository
from typing import Optional
from uuid import uuid4
from hashlib import sha256

@dataclass
class Athlete:
    id: str
    name: str
    nationality: str
    age: int
    
@dataclass
class AthleteRepository(Repository):
    db: DB
    
    def __init__(self):
        self.db = db
    
    def create(self, **attrs) -> Optional[Athlete]:
        id = str(attrs.get('id'))
        name = attrs.get('name')
        nationality = attrs.get('nationality')
        age = attrs.get('age')
        
        result = self.db.execute(
            "INSERT INTO athlete VALUES (?, ?, ?, ?)",
            (str(id), str(name), str(nationality), str(age))
        )
        if result is None:
            return None
        
        if result is not None:
            return self.read(id=id)
        
    def read(self, id) -> Optional[Athlete]:
        id = str(id)        
        result = self.db.execute(
            "select * from athlete where id = ?",
            (id,)
        )
        
        if (result is None or result == []):
            return None        

        return Athlete(*result[0])

    def list(self):
        result = self.db.execute(
            "select * from athlete"
        )
        
        if (result is None or result == []):
            return None
        
        return result
    
    def update(self, athlete: Athlete, **attrs) -> Optional[Athlete]:

        updates = []
        params = tuple()

        for key, value in attrs.items():
            updates.append(f"{key} = ?")
            params = (*params, value)

        params = (*params, athlete.id)

        update = ", ".join(updates)

        result = self.db.execute(
            f"update athlete set {update} where id = ?",
            params
        )

        if result is None:
            return None

        return self.read(id=id)
    
    def delete(): ...