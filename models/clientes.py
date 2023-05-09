
from config.bd import app, db, ma

class Clientes(db.Model):
    __tablename__ = 'tblclientes'

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    apellidos = db.Column(db.String(50))
    direccion = db.Column(db.String(50))
    descripciondireccion = db.Column(db.String(250))

    def __init__(self, nombre, apellidos, direccion, descripciondireccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion = direccion
        self.descripciondireccion = descripciondireccion

with app.app_context():
    db.create_all()

class ClienteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'apellidos', 'direccion', 'descripciondireccion')