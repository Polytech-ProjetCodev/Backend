# Codev Project : nutritional information by barcode scanning



## How to run
<<<<<<< HEAD
`pip3 install Flask`  
`pip3 install flask-login`  
`pip3 install flask-sqlalchemy`  
`pip3 install pymysql`  
`export FLASK_APP=init.py | flask run`  or `python3 -m flask run` for Python 3  
App is launched on http://localhost:5000/

## Relevant docs
https://pythonhosted.org/Flask-Security/  
https://flask-login.readthedocs.io/en/latest/  
http://flask-sqlalchemy.pocoo.org/2.3/  
http://blog.luisrei.com/articles/flaskrest.html  

## Notes du 8 Décembre 2017
* Vérifier la présence d'allergènes et notifier l'utilisateur
=======
`pip install pipenv`  
`pipenv update`  
`pipenv run python manage.py runserver 8080`
App is launched on http://localhost:8000/

## Relevant docs
https://docs.djangoproject.com/en/2.0/ref/settings/  
https://docs.djangoproject.com/en/2.0/ref/databases/  

## Notes du 8 Décembre 2017
* Vérifier la présence d'allergènes et notifier l'utilisateur
* Configurer PostgresSQL sur Docker  
>>>>>>> 7471fa28bbaf30fd3b1dc0964ea7b1b0860410bb

## Notes du 24 Novembre 2017
* Récupérer Kcal, matières grasses, glucides, sucres, protéines, sel
* Tests sur les codes de retour et tests fonctionnels
* Voir Yuka pour s'inspirer
* OAuth 2 avec Facebook et Google
* Appli multilangue (Anglais, Français, ET ESPAGNOL)
* Faire du release by feature
* Parseur de convert-me.com ?

<<<<<<< HEAD

## Notes du 2/02/2018
* Dockerisation du serveur
* implémentation du serveur GUnicorn à la place du serveur built in django
* regarder Enunciate pour documenter l'API
* regarder OAuth2 en django
* Ecrire test unitaires
=======
## Notes
### Allergènes Openfoodfacts
*	"en:mustard" => Mutarde
* "en:sulphur-dioxide-and-sulphites"
*	"en:nuts" => Noix
*	"en:celery" => Celeri
*	"en:eggs" => Oeufs
*	"en:milk" => Lait
*	"en:soybeans" => Germe de soja
*	"fr:lactosérum"
>>>>>>> 7471fa28bbaf30fd3b1dc0964ea7b1b0860410bb
