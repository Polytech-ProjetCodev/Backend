# Codev Project : nutritional information by barcode scanning



## How to run
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

## Notes du 24 Novembre 2017
* Récupérer Kcal, matières grasses, glucides, sucres, protéines, sel
* Tests sur les codes de retour et tests fonctionnels
* Voir Yuka pour s'inspirer
* OAuth 2 avec Facebook et Google
* Appli multilangue (Anglais, Français, ET ESPAGNOL)
* Faire du release by feature
* Parseur de convert-me.com ?


## Notes du 2/02/2018
* Dockerisation du serveur
* implémentation du serveur GUnicorn à la place du serveur built in django
* regarder Enunciate pour documenter l'API
* regarder OAuth2 en django
* Ecrire test unitaires

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



# TODO
* Add Access-Control-Allow-Origin header on response (See https://github.com/crs4/ome_seadragon/wiki/Enable-Django-CORS-(Cross-Origin-Resource-Sharing)-Headers-configuration)
* Add front_quantity field on component class (1cs, 1cc, ...)
