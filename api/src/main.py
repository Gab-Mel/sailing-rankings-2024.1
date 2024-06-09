
from fastapi import FastAPI, Depends, HTTPException
from database import load_database, load_session
#from nlp import generate_questions
from models import AtletaModel, RankingEloModel, final_dataModel, CompeticaoModel
import select_xml as xml
from pydantic import BaseModel
from sqlalchemy.orm import Session, joinedload
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

#load_database()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    load_database()

class CreateDocumentModel(BaseModel):
    title: str
    content: str
"""
@app.post("/documents", status_code=201)
async def create_document(document: CreateDocumentModel = None, db: Session = Depends(load_session)):
    document = DocumentModel(title=document.title, content=document.content)
    db.add(document)
    db.commit()

    return {"id": document.id}
"""

class CreateRankingEloModel(BaseModel):
    name: str
    
@app.post("/ranking", status_code=201)
async def create_ranking(listRanking = None, db: Session = Depends(load_session)):
    atletas = xml.atleta()
    competicoes = xml.competicoes()
    final_data = xml.sumulas()
    
    """
    for i in range(len(atletas)):
        document = AtletaModel(id=int(atletas['ID Competidor'][i]), 
                               name=atletas['Nome Competidor'][i])
        db.add(document)
        db.commit()
    
    for i in range(len(competicoes)):
        document = CompeticaoModel(id=int(competicoes['ID Competição'][i]), 
                                   name=competicoes['Nome Competição'][i])
        db.add(document)
        db.commit()
    
    for i in range(len(final_data)):
        document = final_dataModel(id=int(final_data['ID Resultado'][i]), 
                                   id_atleta=int(final_data['ID Competidor'][i]), 
                                   id_competicao=int(final_data['ID Competição'][i]), 
                                   classe_vela=final_data['Classe Vela'][i], 
                                   pontuacao_regata=final_data['Pontuação Regata'][i], 
                                   descarte=int(final_data['Descarte'][i]), 
                                   flotilha=final_data['Flotilha'][i], 
                                   posicao=int(final_data['Posição Geral'][i]), 
                                   punicao=final_data['Punição'][i], 
                                   pontuacao_total=int(final_data['Pontuação Total'][i]), 
                                   nett=int(final_data['Nett'][i]))
        db.add(document)
        db.commit()
    """
    ranking = xml.ranking_elo_40_49ER()
    for i in range(len(ranking)):
        document = RankingEloModel(name=ranking['Unnamed: 0'][i], 
                                   score = float(ranking['Rating'][i]),
                                   classe = '49ER',
                                   ano = 2024)
        db.add(document)
        db.commit()
        
    ranking = xml.ranking_elo_40_49ERFX()
    for i in range(len(ranking)):
        document = RankingEloModel(name=ranking['Unnamed: 0'][i], 
                                   score = float(ranking['Rating'][i]),
                                   classe = '49ERFX',
                                   ano = 2024)
        db.add(document)
        db.commit()
    
    ranking = xml.ranking_elo_ILCA_6()
    for i in range(len(ranking)):
        document = RankingEloModel(name=ranking['Unnamed: 0'][i], 
                                   score = float(ranking['Rating'][i]),
                                   classe = 'ILCA 6',
                                   ano = 2024)
        db.add(document)
        db.commit()
    
    ranking = xml.ranking_elo_ILCA_7()
    for i in range(len(ranking)):
        document = RankingEloModel(name=ranking['Unnamed: 0'][i], 
                                   score = float(ranking['Rating'][i]),
                                   classe = 'ILCA 7',
                                   ano = 2024)
        db.add(document)
        db.commit()
    
    

"""
@app.get("/documents")
async def get_documents(db: Session = Depends(load_session)):
    return db.query(DocumentModel).all()
"""
@app.get("/ranking")
async def get_ranking(db: Session = Depends(load_session)):
    return db.query(RankingEloModel).all()

"""
@app.get("/documents/{document_id}")
async def get_document(document_id: int, db: Session = Depends(load_session)):
    document = db.query(DocumentModel).filter(DocumentModel.id == document_id).options(
        joinedload(DocumentModel.questions)
    ).first()

    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    return document

@app.get("/documents/{document_id}/questions")
async def get_questions(document_id: int, db: Session = Depends(load_session)):
    document = db.query(DocumentModel).get(document_id)

    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")

    text = document.content
    questions = generate_questions(text, 10)

    return questions

class CreateQuestionModel(BaseModel):
    text: str

@app.post("/documents/{document_id}/questions", status_code=201)
async def create_question(document_id: int, question: CreateQuestionModel, db: Session = Depends(load_session)):
    document = db.query(DocumentModel).get(document_id)

    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")

    question = QuestionModel(text=question.text, document_id=document_id)
    db.add(question)
    db.commit()

    return {"id": question.id}
"""
