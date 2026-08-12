from flask_restful import Resource
from flask import request, jsonify, make_response
from marshmallow import ValidationError
from src.schemas.produto_schemas import (
    produto_schema, produtos_schema
    )
from src.services import produto_services
from src import api

class ProdutoList(Resource):
    def get(self):
        produtos = produto_services.listar_produto()

        if not produtos:
            return make_response(jsonify({'message': 'Não existem produtos'}), 404)

        return make_response(jsonify(produtos_schema.dump(produtos)), 200)

    def post(self):
        try:
            produto = produtos_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        if produto_services.listar_produto_por_id(produto.id):
            return {'message' : 'Email já cadastrado!'}, 409

        try:
            resultado = produto_services.criar_produto(produto)

            return produto.dump(resultado),201
        
        except Exception as e:
            return {
                "message":str(e)
            }, 400
            

api.add_resource(ProdutoList, '/produtos')


class ProdutoResource(Resource):

    def get(self, id_produto):
        produto = produto_services.listar_produto_por_id(id_produto)

        if not produto:
            return{"message": "Produto não encontrado"}, 404

        
    def put(self, id_produto):
        try:
            novo_produto = produtos_schema.load(request.get_json())

        except ValidationError as err:

         produto = produto_services.editar_usuario(
            id_produto = {
                "nome_produto":novo_produto.nome_produto,
                "uni_medida":novo_produto.uni_medida,
                "vlr_unitario":novo_produto.vlr_unitario,
                "qtd_estoque":novo_produto.qtd_estoque
            }
        )
         if not produto:
             return{"message": 'Produto não encontrado'}, 404

        
    def delete(self, id_produto):
        if produto_services.deletar_produto(id_produto):
            return {
                "message" : 'Produto deletado com sucesso'
            },

api.add_resource(ProdutoResource, '/produto/<int:id_usuario>')

