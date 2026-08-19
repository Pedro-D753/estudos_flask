from flask import Flask
from connection import db, Config, ma
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flasgger import Swagger

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

    swagger = Swagger(app, config={
        # configuração de cabeçalho
        "headers":[],
        "specs":[
            {
                # http://localhost:5000/apispec.json
                "endpoint":"apispec",
                "route":"/apispec.json"
                "rule_filter": lamda rule:True,
                
                "model_filter": lamda tag: True

            }
        ],
        "static_url_path":"/flasgger_static",
        "swagger_ui": True,
        "specs_route":"/docs"
    })
    
    
    @app.get('/')
    def home():
        return {"mensagem": "API Flask funcionando"},200
    
    return app