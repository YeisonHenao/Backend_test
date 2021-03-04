import flask
from flask import request
from flask import jsonify

app = flask.Flask(__name__)

app.config['DEBUG'] = True

@app.route('/',methods=['GET'])
def root():
    return "Hola mundo!"

@app.route('/Home',methods=['GET'])
def Home():
    return "Hola Home!"

@app.route('/Login',methods=['GET'])
def Login():
    persona = request.args.get('usuario')
    clave = request.args.get('clave')
    if persona == 'usuario' and clave == 'clave':
        return "Bienvenido usuario"
    else:
        return "Revisar credenciales"


app.run()
