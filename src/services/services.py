from flask import Flask

app = Flask(__name__)

@app.post("create_user")
def criar_usuario():
    ...
    
    
@app.get("read_user")
def listar_usuario():
    ...
    
    
@app.delete("delete_user")
def deletar_usuario():
    ...
    
    
@app.put("edit_user")
def editar_usuario():
    ...
    
    
