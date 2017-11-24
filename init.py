from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
# from flask_request_params import bind_request_params
import requests
import re
import json

# import LoginManager


app = Flask(__name__)

# Configure database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://codev_back_user:W?9422$8+},3>3378@localhost[:3306]/codev_back'
db = SQLAlchemy(app)

# app.before_request(bind_request_params)


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


@app.route('/recipe/compute', methods=['GET'])
def computeRecipe():
    """this route takes in parameter a bunch of components, with their quantity, and return the amount of fat it contains."""
    total_fat = 0
    for component in request.args.getlist('component'):
        component = component.split('|')
        component_id, quantity = component[0], component[1]
        total_fat += get_component_fat(component_id, float(quantity))
    return str(total_fat)


def get_component(component_id):
    """returns a dictionnary containing all information provided by the openfoodfacts.org API from the ID passed in parameter"""
    return requests.get('https://fr.openfoodfacts.org/api/v0/produit/' + str(component_id) + '.json').json()


def get_component_name(component_id):
    """returns the name of the product of which the ID was passed in parameter"""
    component = get_component(component_id)
    return component['product']['product_name_en']


def get_component_fat(component_id, quantity=100):
    """returns the amount of fat by 100g of the product of which the ID was passed in parameter"""
    component = get_component(component_id)
    fat100g = component['product']['nutriments']['fat_100g']
    return fat100g / 100 * quantity
