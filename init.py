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


@app.route("/test")
def test():
    return get_component_name('009800892204') + str(get_component_fat('009800892204'))


# just return request.params
# Example : curl -X POST http://localhost:5000/recipe/compute -d 'components[009800892204]=100g&components[009800892204]=10g'
@app.route('/recipe/compute', methods=['GET'])
def computeRecipe():
    for component in request.args.getlist('component'):
        fat_value = get_component_fat(component)
        print(component)
        print(fat_value)

    return (str(component))




def get_component(component_id):
    return requests.get('https://fr.openfoodfacts.org/api/v0/produit/' + str(component_id) + '.json').json()

def get_component_name(component_id):
    component = get_component(component_id)
    return component['product']['product_name_en']

def get_component_fat(component_id, quantity=100):
    component = get_component(component_id)
    fat100g = component['product']['nutriments']['fat_100g']
    return fat100g / 100 * quantity

def get_recipe_fat(components_id):
    total_fat = 0
    for component_id in components_id:
        total_fat += get_component_fat(component_id)
