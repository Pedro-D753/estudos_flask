from connection import db
from passlib import CryptContext
from sqlalchemy import Column, Integer, String, Float, DateTime

class Produto(db.Model):
    __tablename__ == 'produtos'

    id_produto = db.Column(Integer, primary_key=True, autoincrement=True)
    nome = db.Column(String(100), nullable=False)
    uni_medida = db.Column(String(10), nullable=False)
    vlr_unitario = db.Column(Float, nullable=False)

    fk_categoria_id = db.Column(db.Integer, db.ForeignKey("categorias_id"), nullable=False)

    categorias = db.relationship("Categoria", back_populates='produtos')
