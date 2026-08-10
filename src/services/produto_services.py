from ..models.produto_model import ProdutoModel
from ..models.registro_model import RegistroModel
from connection import db

def criar_produto(produto):
    produto_db = ProdutoModel(nome=produto.nome_produto, uni_medida=produto.uni_medida, valor_unitario=produto.valor_unitario, qtd_estoque=produto.qtd_estoque)
    db.session.add(produto_db)
    db.session.commit()
    return produto_db
    
    
def listar_produto():
    return ProdutoModel.query.all()


def listar_produto_por_id(id):
    usuario_encontrado = ProdutoModel.query.get(id)
    return usuario_encontrado


def listar_produto_por_categoria(categoria):
    return ProdutoModel.query.filter_by(categoria=categoria).first()


def deletar_produto():
    produto = ProdutoModel.query.get(id)
    if produto:
        db.session.delete(produto)
        db.session.commit()
        return True
    return False
    
    
def editar_produto(id, novo_produto):
    produto = ProdutoModel.query.get(id)
    if produto:
        produto.nome = novo_produto['nome']
        produto.uni_medida = novo_produto['uni_medida']
        produto.valor_unitario = novo_produto['valor_unitario']
        produto.qtd_estoque = novo_produto['qtd_estoque']
        db.session.commit()
        return produto
    return None
    

