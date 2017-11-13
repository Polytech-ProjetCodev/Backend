from flask import Flask
import requests
import json
import LoginManager
app = Flask(__name__)

@app.route("/")
def hello():
    login_manager = LoginManager()
    login_manager.init_app(app)
    return "Hello World!"

@app.route("/coucou/<string:username>")
def coucou(username):
    return "Coucou %s" % username

@app.route("/coucou/<string:username>")
def coucou(username):
    return "Coucou %s" % username

@app.route("/yolo")
def yolo():
    response = requests.get('https://fr.openfoodfacts.org/api/v0/produit/009800892204.json')
    print (type(response.json()))
    # json.loads(response)
    return response.json()['product']['packaging']
