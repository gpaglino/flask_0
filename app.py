from flask import Flask ,jsonify, request
from markupsafe import escape


app = Flask(__name__)

# como se crean las rutas, con un dercorador @, con el objeto app, y route, que es lo que vamos a poner a continuacion de la sintasis que escribimos que finaliza con por 5000

@app.route('/')
def index():
    return 'Index'

@app.route("/ping")
def ping():
    return jsonify({"mensaje" :"pong"})

@app.route('/usuarios/<string:nombre>')
def usuario_by_name(nombre):
    return jsonify({"name": nombre})

@app.route('/usuarios/<int:id>')
def usuarios_by_id(id):
    return jsonify({"id": id})

@app.route('/<path:nombre>')
def no_hacer(nombre):
    return escape(nombre)

#GET todos los recursos
@app.route('/recurso', methods = ['GET'])
def get_recursos():
    return jsonify({"data": "lista de todos los items de este recurso"})

# POST NUEVO 'RECURSOS'
@app.route('/recurso', methods = ['POST'])
def post_recursos():
    print(request.get_json())
    body = request.get_json()
    #cree la variable auxiliar body
    name = body["name"]
    modelo = body["modelo"]
    #name = request.get_json()["name"]
    #modelo = request.get_json()["modelo"]

    #insertar en la BD
    return jsonify({"recurso": {
        "name": name,
        "modelo": modelo
    }})
# GET un 'recurso' a traves de su id
@app.route('/recurso/<int:id>', methods = ['GET'])
def get_recurso_by_id(id):
    #Buscar en la bd un registro con ese id
    return jsonify({"recurso":{
        "name": "nombre correspondiente a ese id",
        "modelo":"modelo del producto que tiene el id especificado"}})

    
if __name__ =='__main__':
    app.run(debug=True, port=5000)