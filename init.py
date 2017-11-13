from flask import Flask, request, render_template, jsonify
from flask_request_params import bind_request_params
import requests
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
@app.route('/recipe/compute', methods=['GET', 'POST'])
def computeRecipe():
    components = jsonify(request.params)
    nbComponents = len(request.params['components'])
    for x in range(0, nbComponents):
        print (components[x][0])
        #getFatValue(components(x))
    return 'yolo'


def getFatValue(barcode, quantity):
    response = requests.get('https://fr.openfoodfacts.org/api/v0/produit/' + barcode + '.json')
    fat100g = response.json()['product']['nutriments']['fat_100g']
    return fat100g / 100 * quantity