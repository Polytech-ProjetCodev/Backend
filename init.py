from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/coucou/<string:username>")
def coucou(username):
    return "Coucou %s" % username
