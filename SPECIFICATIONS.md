# Codev Project : nutritional information by barcode scanning
(Basé sur le cahier des charges de M. Amaury Codina)


## Présentation du sujet
L’objectif de ce projet est de concevoir par groupe de 2 ou 3 étudiants la partie serveur/Backend d’un service et la partie cliente/Frontend qui appellera ce service.  
Le Backend se basera au choix sur une technologie au choix (ici **Python avec Django**). La partie Frontend sera une application **Ionic**.

## Application recipe calculator
### Contexte
Puisque nous devons nous nourrir, l’alimentation est un sujet crucial dans nos vies. Cependant,
bonnes habitudes alimentaires sont à la mode de nos jours.
L’idée principale de l’application est de pouvoir, à travers une interface ergonomique et simple,
connaître les principales valeurs nutritionnelles d’une recette en indiquant les ingrédients et leur
quantité. L’ajout d’un ingrédient à la recette se fait via le code-barre du produit, ou le cas échéant via
une saisie (pseudo) manuelle de ses informations nutritionnelles.
Les informations nutritionnelles des produits proviennent de la base de données Open Food Facts qui
recense de manière collaborative les produits vendus dans le monde. Celle-ci donne des informations
sur
Exemple d’une application sur le même principe sans la partie création de recettes, Yuka (disponible
sur le Play Store et l’Apple Store).

### Cas d'utilisation
Lors de la première utilisation, l’utilisateur devra se créer un compte. Ce compte peut être
uniquement lié à l’application ou bien il peut s’agir d’une authentification OAuth 2.0.
Un utilisateur scanne les codes-barres des ingrédients qu’il va utiliser.
Pour chaque produit scanner l’utilisateur rentre sa quantité (ex : 200 grammes, 3 oeufs, une cuillère à
soupe, etc.).
Une fois la recette validée, un résumé s’affiche et résume les informations de la recette avec
notamment un aperçu des métriques nutritionnelles pour 100 grammes.
L’utilisateur peut sauvegarder la recette, la modifier ou bien la supprimer.
La sauvegarde se fait en ligne et est rattachée au compte utilisateur.
L’utilisateur peut partager une recette créée à une personne.

## Cahier des charges
### Obligatoire
* Application mobile Android native ou hybride (**Ionic**).
* Calcul des informations nutritionnelles des recettes avec au moins comme données : calories,
protéines, glucides (dont les sucres), lipides (acides gras saturés), sel, fibres.
* Utilisation de la caméra pour scanner des codes-barres et ajouter des ingrédients (API Open Food
Facts) ou ajout à la main (qui seront stockés en BDD/en ligne).
* Compte utilisateur
* Compte propre à l’application et/ou
* Compte issu d’une authentification OAuth 2.0 (Microsoft, Google, Facebook, Twitter)
* Partage de recettes à un ami via une solution au choix (Web Service, fichier json, etc.)
* Stockage en ligne des recettes créées par l’utilisateur

### Bonus
* Application multilingue (Français, Anglais, **Espagnol**)
* Logo & nom pour l'application réfléchis et stylés
* Utilisation des notifications Push (Firebase ou GCM)
* Pré-reconnaissance d’une recette en la copiant/collant d’un site (ex : Marmiton).
* Peut fonctionner en local (consultation de recettes déjà crées hors connexion) base de données
SQLite avec Room par exemple

### Idée perso
* L'utilisateur configure ses allergènes et est notifié lorsqu'une recette en contient au moins un.


### Autres
Code couleur pour les types de recettes
