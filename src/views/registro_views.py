from flask_restful import Resource
from flask import request, jsonify, make_response
from marshmallow import ValidationError
from src.schemas.registro_schemas import (
    registro_schema, registros_schemas
    )
from src.services import registro_services
from src import api

class RegistroList(Resource):
    def get(self):
        """
        Lista todos os registros
        ---

        tags:
        - Registros
        responses:
          200:
            description: Lista de Registros
          404:
            description: Nenhum registro encontrado
        """

        registros = registro_services.listar_registro()

        if not registros:
            return make_response(jsonify({'message': 'Não existem registros'}), 404)

        return make_response(jsonify(registro_schema.dump(registros)), 200)

    def post(self):
        """
        Cadastrar um novo registro
        ---
        
        tags:
        -- Registros
        parameters:
          - in: body
          name: body
          required: True
          schema: 
            type: object
            properties:
              nome:
                type: string
                example: Pedro D.
              email:
                type: string
                example: pedro@email.com
              senha: senha678
        responses:
          201:
            description: Usuário cadastrado
          400:
            description: Erro de validação
          409:
            description: Email já cadastrado
        """    

        try:
            registro = registro_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        if registro_services.listar_registro_por_id(registro.id):
            return {'message' : 'Email já cadastrado!'}, 409  #Corrigir isso depois

        try:
            resultado = registro_services.criar_registro(registro)

            return registro_schema.dump(resultado),201
        
        except Exception as e:
            return {
                "message":str(e)
          }, 400
            


api.add_resource(RegistroList, '/registros')


class RegistroResource(Resource):

    def get(self, id_registro):
        """
        Buscar registro por ID
        ---
        tags:
          - Registro
        parameters:
        - name
        int: path
        type: integer
        required: True
        schema:
          type: object
          properties:
            data_registro: 
              type: datetime
            tipo:
              type: string
        responses:

        """
        registro = registro_services.listar_registro_por_id(id_registro)

        if not registro:
            return{"message": "Registro não encontrado"}, 404

        
    def put(self, id_registro):
        """
        Editar usuarios
        ---
        tags:
          -- usuarios
        parameters
            name: id_usuario
            in: integer
            type: integer
            required: True
            schema:
              type: object
              properties:
                nome:
                  type: string
                emal:
                  type: string
                senha:
                  type: string
        responses:
           200:
            description: Update 
           404:
            description: usuario não encontrado
        """

        try:
            novo_registro = registro_schema.load(request.get_json())

        except ValidationError as err:

         registro = registro_services.editar_registro
         (
            id_usuario = {
                "nome":novo_usuario.nome,
                "email":novo_usuario.email,
                "senha":novo_usuario.senha
            }
        )
         if not registro:
             return{"message": "Registro não encontrado"}, 404

        
    def delete(self, id_registro):
        """
        Deletar registro
        ---
        tags:
          - registro
        parametes:
            name: id_registro
            in: path
            type: integer
            required: True
        responses:
           200:
            description: Registro deletado com sucesso
           404:
           description: Registro não encontrado
        
        """

        if registro_services.deletar_registro(id_registro):
            return {
                "message" : 'Registro deletado com sucesso'
            },404

api.add_resource(RegistroResource, '/registro/<int:id_registro>')

