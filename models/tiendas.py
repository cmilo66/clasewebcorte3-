from config.bd import app, db, ma

class Tiendas(db.Model):
    __tablename__ = 'tbltiendas'

    id  = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    direccion = db.Column(db.String(50))
    telefono = db.Column(db.String(10))

    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

with app.app_context():
    db.create_all()

class TiendasSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'direccion', 'telefono')