from flask import Blueprint, request, json, jsonify, render_template
from config.bd import app, db, ma

route_pedidos = Blueprint('route_pedidos', __name__)

@route_pedidos.route("/savepedidos", methods=['POST'])
def savepedidos():
    return "guardado"