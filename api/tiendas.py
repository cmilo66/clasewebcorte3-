from flask import Blueprint, request, json, jsonify, render_template
from config.bd import app, db, ma

route_tiendas = Blueprint('route_tiendas', __name__)

@route_tiendas.route("/savetiendas", methods=['POST'])
def savetiendas():
    return "guardado"