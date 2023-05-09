from flask import Blueprint, request, json, jsonify, render_template
from config.bd import app, db, ma

route_clientes = Blueprint('route_cliente', __name__)

@route_clientes.route("/savecliente", methods=['POST'])
def savecliente():
    return "guardado"