from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.bd import db, app, ma

from api.clientes import route_clientes
from api.tiendas import route_tiendas
from api.pedidos import route_pedidos
app.register_blueprint(route_clientes, url_prefix="/api")

app.register_blueprint(route_pedidos, url_prefix="/api")
@app.route('/', methods=['GET'])
def index():
    return "Prueba"

if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')
    