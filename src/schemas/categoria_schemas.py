from src import ma
from src.models import categoria_model
from marshmallow import fields

class CategoriaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = categoria_model.CategoriaModel
        load_instance = True
        