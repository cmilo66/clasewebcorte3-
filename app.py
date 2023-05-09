from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.bd import db, app, ma

@app.route('/', methods=['GET'])
def index():
    return "Prueba"

if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')
    