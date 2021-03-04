import flask
import flask_cors
from flask_cors import CORS
from flask import request, jsonify, Response, make_response


app = flask.Flask(__name__)
CORS(app)
app.config['DEBUG'] = True


@app.route('/', methods=['GET'])
def root():
    return "Hola mundo!"


@app.route('/Home', methods=['GET'])
def Home():
    return "Hola Home!"


@app.route('/Login', methods=['POST'])
def Login():
    content = request.json
    if content['usuario'] == 'usuario' and content['clave'] == '123456':
        return Response("Usuario y clave correctos", status=200)
    else:
        return Response("Verifica las credenciales", status=401)


app.run()
