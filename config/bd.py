from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:secret@adso_mysql/webavan'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


app.secret_key = "webulava"

db = SQLAlchemy(app)

ma = Marshmallow(app)