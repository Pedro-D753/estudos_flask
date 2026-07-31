from flask import Flask

app = Flask(__name__)

@app.post("criar_usuario")
def criar_usuario():