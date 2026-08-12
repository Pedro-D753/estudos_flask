from ..models.registro_model import RegistroModel
from connection import db

def criar_registro(registro):
    registro_db = RegistroModel(dth_registro=registro.dth_registro, tipo=registro.tipo)
    db.session.add(registro_db)
    db.session.commit()
    return registro_db
    
    
def listar_registro():
    return RegistroModel.query.all()


def listar_registro_por_id(id):
    registro_encontrado = RegistroModel.query.get(id)
    return registro_encontrado

        
def deletar_registro():
    registro = RegistroModel.query.get(id)
    if registro:
        db.session.delete(registro)
        db.session.commit()
        return True
    return False
    
    
def editar_registro(id, novo_registro):
    registro =  RegistroModel.query.get(id)
    if registro:
        registro.dth_registro = novo_registro['dth_registro']
        registro.tipo = novo_registro['tipo']
        db.session.commit()
        return registro
    return None
    
