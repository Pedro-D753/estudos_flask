from ..models.usuario_model import UsuarioModel
from connection import db

def criar_usuario(usuario):
    usuario_db = UsuarioModel(nome=usuario.nome, email=usuario.email)
    usuario_db.gen_senha(usuario.senha)
    db.session.add(usuario_db)
    db.session.commit()
    return usuario_db

    
def listar_usuario():
    return UsuarioModel.query.all()


def listar_usuario_por_id(id):
    usuario_encontrado = UsuarioModel.query.get(id)
    return usuario_encontrado


def listar_por_email(email):
   return UsuarioModel.query.filter_by(email=email).first()
    
    
def deletar_usuario():
    usuario = UsuarioModel.query.get(id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return True
    return False
    
    
def editar_usuario(id, novo_usuario):
    usuario = UsuarioModel.query.get(id)
    if usuario:
        usuario.nome = novo_usuario['nome']
        usuario.email = novo_usuario['email']
        if novo_usuario.get('senha'):
            usuario.gen_senha(novo_usuario['senha'])

        db.session.commit()
        return usuario
    return None
    
    
