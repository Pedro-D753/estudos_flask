from src import ma
from src.models import registro_model
from marshmallow import fields,  validate, ValidationError, validates
from datetime import datetime

class RegistroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = registro_model.RegistroModel
        fields = ('id_registro', 'dth_registro', 'tipo')

    data_registro = fields.DateTime(required=True)
    tipo = fields.String(required=True, validate=validate.OneOf(
       ['Escritório e Administrativo', 
        'Limpeza e Copa', 'Manutenção e Segurança'],
        error= 'Tipo de produto de almoxarifado inválido'
                                                                ))
    
    @validates('dth_registro')
    def menos_que_agora(self, value):
        agora = datetime.now(value.tzinfo)
        
        if value > agora:
            raise ValidationError("A data de registro não pode estar no futuro.")
