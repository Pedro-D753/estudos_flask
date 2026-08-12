from src import ma
from src.models import usuario_model
from marshmallow import fields

class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = usuario_model.UsuarioModel
        load_instance = True
        fields = ('id', 'nome', 'email', 'senha')


    nome = fields.String(required=True)
    email = fields.Email(required=True)
    senha = fields.String(required=True)

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)