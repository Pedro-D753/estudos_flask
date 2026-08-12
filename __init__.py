from flask import Flask
from connection import db, Config, ma
from flask_marshmallow import Marshmallow
from flask_restful import Api

ma = Marshmallow()
api = Api()

from models.usuario_model import UsuarioModel
from views import usuario_view

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)
    
    
    @app.get('/')
    def home():
        return {"mensagem": "API Flask funcionando"},200
    
    return app