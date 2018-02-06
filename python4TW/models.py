from django.db import models
import requests
# class Allergen(models.Model):
#     name = models.CharField(max_length=45)


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
        self.image = full_information['product']['image_front_url']
        self.energy_100g = full_information['product']['nutriments']['energy_100g']
        self.fat_100g = full_information['product']['nutriments']['fat_100g']
        self.saturated_fat_100g = full_information['product']['nutriments']['saturated-fat_100g']
        self.carbohydrates_100g = full_information['product']['nutriments']['carbohydrates_100g']
        self.sugar_100g = full_information['product']['nutriments']['sugars_100g']
        self.protein_100g = full_information['product']['nutriments']['proteins_100g']
        self.salt_100g = full_information['product']['nutriments']['salt_100g']


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    favorite = models.BooleanField()
    owner = models.ForeignKey(
        'auth.User', related_name="recipes", on_delete=models.CASCADE)


class Component(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        Recipe, related_name='components', on_delete=models.CASCADE)
    quantity = models.FloatField()
