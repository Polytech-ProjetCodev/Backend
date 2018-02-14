from django.db import models
import requests
#TokenAuth imports
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
# class Allergen(models.Model):
#     name = models.CharField(max_length=45)

#Triggers when a User is created, and allocates it a token
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Ingredient(models.Model):
    barcode = models.CharField(max_length=13, primary_key=True)
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    energy_100g = models.FloatField()
    fat_100g = models.FloatField()
    saturated_fat_100g = models.FloatField()
    carbohydrates_100g = models.FloatField()
    sugar_100g = models.FloatField()
    protein_100g = models.FloatField()
    salt_100g = models.FloatField()

    def get_full_information(self, barcode):
        """returns a dictionnary containing all information provided by the openfoodfacts.org API from the ID passed in parameter"""
        openfoodfactsinfo = requests.get(
            'https://fr.openfoodfacts.org/api/v0/produit/' + str(barcode) + '.json').json()
        return openfoodfactsinfo

    def get_information(self, barcode):
        full_information = self.get_full_information(barcode)
        self.barcode = barcode
        self.name = full_information['product']['product_name']

        try:
            self.image = full_information['product']['image_front_url']
        except KeyError:
            self.image = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"

        try:
            self.energy_100g = full_information['product']['nutriments']['energy_100g']
        except KeyError:
            self.energy_100g = -1

        try:
            self.fat_100g = full_information['product']['nutriments']['fat_100g']
        except KeyError:
            self.fat_100g = -1

        try:
            self.saturated_fat_100g = full_information['product']['nutriments']['saturated-fat_100g']
        except KeyError:
            self.saturated_fat_100g = -1

        try:
            self.carbohydrates_100g = full_information['product']['nutriments']['carbohydrates_100g']
        except KeyError:
            self.carbohydrates_100g = -1

        try:
            self.sugar_100g = full_information['product']['nutriments']['sugars_100g']
        except KeyError:
            self.sugar_100g = -1

        try:
            self.protein_100g = full_information['product']['nutriments']['proteins_100g']
        except KeyError:
            self.protein_100g = -1

        try:
            self.salt_100g = full_information['product']['nutriments']['salt_100g']
        except KeyError:
            self.salt_100g = -1


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    favorite = models.BooleanField()
    owner = models.ForeignKey(
        'auth.User', related_name="recipes", on_delete=models.CASCADE)
    energy = models.FloatField()
    fat = models.FloatField()
    saturated = models.FloatField()
    carbohydrates = models.FloatField()
    sugar = models.FloatField()
    protein = models.FloatField()
    salt = models.FloatField()

class Component(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey( Recipe, related_name='components', on_delete=models.CASCADE)
    quantity = models.FloatField()