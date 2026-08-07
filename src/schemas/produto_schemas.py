from src import ma
from src.models import produto_model
from marshmallow import fields, validate
from .categoria_schemas import CategoriaSchema


class ProdutoSchema(ma.SQLAlchemyAutoSchema):
    categoria = fields.Nested(CategoriaSchema, dump_only=True)
    
    class Meta:
        model = produto_model.ProdutoModel
        load_instance = True
        include_fk = True
        fields = ('id_produto', 'nome_produto', 'uni_medida', 'vlr_unitario' 'qtd_estoque')

    uni_medida = fields.String(
        required=True,
        validate=validate.OneOf(
            ['UN', 'KG', 'L' 'CX'],
            error= 'Unidade de medida inválida'
        )
    )


produto_schema = ProdutoSchema(many=True)

nome_produto = fields.String(
    required=True,
    validate=validate.Length(
        min='3' ,
        error= 'O nome deve ter no mínimo 3 letras'
    ))


vlr_unitario = fields.Decimal(
    required=True,
    places=2,
    validate=validate.Range(
    min=0, 
    error='O valor unitario deve ser maior ou igual a 0.')
    )


categoria = fields.Nested(
    CategoriaSchema,
      dump_only=True)

quantidade_estoque = fields.Integer(
    required=True,
    validate=validate.Range(
        min=0,
        error= "O valor deve ser maior ou igual a 1"
    ))

