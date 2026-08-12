from flask_restful import Resource
from flask import request, jsonify, make_response
from marshmallow import ValidationError
from src.schemas.usuario_schemas import (
    usuario_schema, usuarios_schema
    )
from src.services import usuario_services
from src import api

class UsuarioList(Resource):
    def get(self):
        usuarios = usuario_services.listar_usuario()

        if not usuarios:
            return make_response(jsonify({'message': 'Não existem usuários'}), 404)

        return make_response(jsonify(usuarios_schema.dump(usuarios)), 200)

    def post(self):
        try:
            usuario = usuarios_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        if usuario_services.listar_por_email(usuario.email):
            return {'message' : 'Email já cadastrado!'}, 409

        try:
            resultado = usuario_services.criar_usuario(usuario)

            return usuarios_schema.dump(resultado),201
        
        except Exception as e:
            return {
                "message":str(e)
            }, 400
            


api.add_resource(UsuarioList, '/usuarios')


class UsuarioResource(Resource):

    def get(self, id_usuario):
        usuario = usuario_services.listar_usuario_por_id(id_usuario)

        if not usuario:
            return{"message": "Usuario não encontrado"}, 404

        
    def put(self, id_usuario):
        try:
            novo_usuario = usuarios_schema.load(request.get_json())

        except ValidationError as err:

         usuario = usuario_services.editar_usuario(
            id_usuario = {
                "nome":novo_usuario.nome,
                "email":novo_usuario.email,
                "senha":novo_usuario.senha
            }
        )
         if not usuario:
             return{"message": "Usuario não encontrado"}, 404

        
    def delete(self, id_usuario):
        if usuario_services.deletar_usuario(id_usuario):
            return {
                "message" : 'Usuário deletado com sucesso'
            },404

api.add_resource(UsuarioResource, '/usuario/<int:id_usuario>')

