from connection import db
from passlib import CryptContext
from sqlalchemy import Column, Integer, String, Float, DateTime

class RegistroModel(db.Model):
    __tablename__ == 'produtos'

    id_registro = db.Column(Integer, primary_key=True, autoincrement=True)
    dth_registro = db.Column(DateTime, nullable=False)
    tipo = db.Column(String(120), nullable=False)
