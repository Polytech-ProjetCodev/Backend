from flask import Flask, request, render_template, jsonify
# from flask_request_params import bind_request_params
import requests
import re
import json

# import LoginManager


app = Flask(__name__)
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
    return get_ingredient_name('009800892204') + str(get_ingredient_fat('009800892204'))


@app.route('/recipe/compute', methods=['GET'])
def computeRecipe():
    """this route takes in parameter a bunch of ingredients, with their quantity, and return the amount of fat it contains."""
    total_fat = 0
    for ingredient in request.args.getlist('ingredient'):
        ingredient = ingredient.split('|')
        ingredient_id, quantity = ingredient[0], ingredient[1]
        total_fat += get_ingredient_fat(ingredient_id, float(quantity))
    return str(total_fat)


def get_ingredient_by_id(ingredient_id):
    """returns a dictionnary containing all information provided by the openfoodfacts.org API from the ID passed in parameter"""
    return requests.get('https://fr.openfoodfacts.org/api/v0/produit/' + str(ingredient_id) + '.json').json()


def get_ingredient_name(ingredient_id):
    """returns the name of the product of which the ID was passed in parameter"""
    ingredient = get_ingredient_by_id(ingredient_id)
    return ingredient['product']['product_name_en']


def get_ingredient_fat(ingredient_id, quantity=100):
    """returns the amount of fat by 100g of the product of which the ID was passed in parameter"""
    ingredient = get_ingredient_by_id(ingredient_id)
    fat100g = ingredient['product']['nutriments']['fat_100g']
    return fat100g / 100 * quantity

def get_ingredient_salt(ingredient_id, quantity=100):
    """returns the amount of salt by 100g of the product of which the ID was passed in parameter"""
    ingredient = get_ingredient_by_id(ingredient_id)
    salt100g = ingredient['product']['nutriments']['salt_100g']
    return salt100g / 100 * quantity


def get_ingredient_energy(ingredient_id, quantity=100):
    """returns the amount of energy by 100g of the product of which the ID was passed in parameter"""
    ingredient = get_ingredient_by_id(ingredient_id)
    energy100g = ingredient['product']['nutriments']['energy100g']
    return energy100g / 100 * quantity
