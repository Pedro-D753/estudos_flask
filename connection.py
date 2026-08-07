from dotenv import load_dotenv
import os
from flask_marshmallow import Marshmallow

from flask_sqlalchemy import SQLAlchemy

load_dotenv()

db = SQLAlchemy()
ma = Marshmallow()

class Config:
    SQLALCHEMY_DATABASE_URL=os.get('URL_DATABASE')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False