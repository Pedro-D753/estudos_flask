from connection import db
from passlib import CryptContext
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean

class CategoriaModel(db.Model):
    __tablename__ = 'categoria'

    id_categoria = db.Column(Integer, primary_key=True, autoincrement=True)
    tipo = db.Column(Boolean, nullable=False)


        
