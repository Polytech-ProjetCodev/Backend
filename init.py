from flask import Flask, request, render_template, jsonify
from flask_request_params import bind_request_params
import requests
import re
import json

# import LoginManager
app = Flask(__name__)
app.before_request(bind_request_params)


@app.route("/")
def hello():
    # login_manager = LoginManager()
    # login_manager.init_app(app)
    return "Hello World!"


@app.route("/coucou/<string:username>")
def coucou(username):
    return "Coucou %s" % username



@app.route("/yolo")
def yolo():
    response = requests.get('https://fr.openfoodfacts.org/api/v0/produit/009800892204.json')
    print (type(response.json()))
    # json.loads(response)
    return response.json()['product']['packaging']


# just return request.params
# Example : curl -X POST http://localhost:5000/recipe/compute -d 'components[009800892204]=100g&components[009800892204]=10g'
@app.route('/recipe/compute', methods=['GET'])
def computeRecipe():

    componentCount =  len(request.args.getlist('component'))
    for i in range(0, componentCount):
        component = request.args.getlist('component')[i]
        print component
        print getFatValue(component)
    return 'yolo'


def getFatValue(bulkComponent):
    barcode = ""
    quantity = ""
    splitComponent = bulkComponent.split('|');
    barcode = splitComponent[0]
    quantity = splitComponent[1]
    print barcode
    print quantity

    quantity = 10

    response = requests.get('https://fr.openfoodfacts.org/api/v0/produit/' + barcode + '.json')
    fat100g = response.json()['product']['nutriments']['fat_100g']
    return fat100g / 100 * quantity
