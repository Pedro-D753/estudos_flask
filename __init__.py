from flask import Flask
from connection import db, Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    
    @app.get('/')
    def home():
        return {"mensagem": "API Flask funcionando"},200
    
    return app