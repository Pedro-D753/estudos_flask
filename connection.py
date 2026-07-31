from dotenv import load_dotenv
import os

from flask_sqlalchemy import SQLAlchemy

load_dotenv()

db = SQLAlchemy()

class Config:
    SQLALCHEMY_DATABASE_URL=os.get('URL_DATABASE')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False