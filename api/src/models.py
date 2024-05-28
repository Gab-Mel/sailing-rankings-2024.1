from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Numeric
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base


class DocumentModel(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    questions = relationship("QuestionModel", back_populates="document", lazy="joined")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
class AtletaModel(Base):
    __tablename__ = "atletas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
class CompeticaoModel(Base):
    __tablename__ = "competicoes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
class final_dataModel(Base):
    __tablename__ = "final_data"

    id = Column(Integer, primary_key=True, index=True)
    id_atleta = Column(Integer, ForeignKey("atletas.id"))
    id_competicao = Column(Integer, ForeignKey("competicoes.id"))
    classe_vela = Column(String, index=True)
    pontuacao_regata = Column(Integer, index=True)
    descarte = Column(Integer, index=True)
    flotilha = Column(String, index=True)
    posicao = Column(Integer, index=True)
    punicao = Column(String, index=True)
    pontuacao_total = Column(Numeric, index=True)
    nett = Column(Integer, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
class RankingEloModel(Base):
    __tablename__ = "ranking_elo"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    score = Column(Numeric, index=True)
    classe = Column(String, index=True)
    position = Column(Integer, index=True)
    ano = Column(Integer, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    


class QuestionModel(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"))
    document = relationship("DocumentModel", back_populates="questions")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
