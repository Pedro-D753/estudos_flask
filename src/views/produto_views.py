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
        """
        Lista todos os produtos
        ---

        tags:
        - Produtos
        responses:
          200:
            description: Lista de Produtos
          404:
            description: Nenhum produto encontrado
        """

        produtos = produto_services.listar_produto()

        if not produtos:
            return make_response(jsonify({'message': 'Não existem produtos'}), 404)

        return make_response(jsonify(produtos_schema.dump(produtos)), 200)

    def post(self):
        """
        Cadastrar um novo produto
        ---
                
        tags:
        -- Produto
        parameters:
        - in: body
        name: body
        required: True
        schema: 
        type: object
        properties:
        nome_produto:
        type: string
        example: produto
        uni_medida:
        type: string
        example: cm
        vlr_unitario: 5
        responses:
        201:
        description: Produto cadastrado
        400:
        description: Erro de validação
    
        """    

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


     """
     Buscar produto por ID
     ---
     tags:
     - Produto
     parameters:
     - name
     int: path
     type: integer
     required: True
     schema:
     type: object
     properties:
     nome_produto: 
     type: string
     uni_medida:
     type: string
     vlr_unitario:
     type: int 
     qtd_estoque:
     type: int
     responses:

    """


     produto = produto_services.listar_produto_por_id(id_produto)

     if not produto:
       return{"message": "Produto não encontrado"}, 404

        
    def put(self, id_produto):
     """
        Editar produtos
        ---
        tags:
          -- Produtos
        parameters
            name: id_produto
            in: integer
            type: integer
            required: True
            schema:
              type: object
              properties:
                nome_produto:
                  type: string
                emal:
                  type: string
                senha:
                  type: string
        responses:
           200:
            description: Usuário editado com sucesso ! 
           404:
            description: Usuário não encontrado
        """


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
        """
        Deletar usuario
        ---
        tags:
          - usuario
        parametes:
            name: id_usuario
            in: path
            type: integer
            required: True
        responses:
           200:
            description: usuario deletado
           404:
           description: usuario nao encontrado
        
        """ 

        if produto_services.deletar_produto(id_produto):
            return {
                "message" : 'Produto deletado com sucesso'
            },

api.add_resource(ProdutoResource, '/produto/<int:id_usuario>')

