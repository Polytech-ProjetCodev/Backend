from django.db import models
# import requests
# from django.contrib.auht.models import User
# Create your models here.

# class Allergen(models.Model):
#     name = models.CharField(max_length=45)

class Ingredient(models.Model):
    barcode = models.CharField(max_length=13, primary_key=True)
    name = models.CharField(max_length=255)
    energy_100g = models.FloatField()
    fat_100g = models.FloatField()
    saturated_fat_100g = models.FloatField()
    carbohydrates_100g = models.FloatField()
    sugar_100g = models.FloatField()
    protein_100g = models.FloatField()
    salt_100g = models.FloatField()


    # def __init__(self, barcode):
    #     self.barcode = barcode
    #     informations = self.get_information()
    #     self.name = informations["name"]
    #     self.energy_100g = informations["energy_100g"]
    #     self.fat_100g = informations["fat_100g"]
    #     self.saturated_fat_100g = informations["saturated-fat_100g"]
    #     self.carbohydrates_100g = informations["carbohydrates_100g"]
    #     self.sugar_100g = informations["sugars_100g"]
    #     self.protein_100g = informations["proteins_100g"]
    #     self.salt_100g = informations["salt_100g"]
    #

    #
    # def __str__(self):
    #     pass
    #
    # def get_information(self):
    #     information = {}
    #     full_information = self.get_full_information()
    #     information["name"] = full_information['product']['product_name_en']
    #     information["energy_100g"] = full_information['product']['nutriments']['energy_100g']
    #     information["fat_100g"] = full_information['product']['nutriments']['fat_100g']
    #     information["saturated-fat_100g"] = full_information['product']['nutriments']['saturated-fat_100g']
    #     information["carbohydrates_100g"] = full_information['product']['nutriments']['carbohydrates_100g']
    #     information["sugars_100g"] = full_information['product']['nutriments']['sugars_100g']
    #     information["proteins_100g"] = full_information['product']['nutriments']['proteins_100g']
    #     information["salt_100g"] = full_information['product']['nutriments']['salt_100g']
    #     return information
    #
    #
    # def get_full_information(self):
    #     """returns a dictionnary containing all information provided by the openfoodfacts.org API from the ID passed in parameter"""
    #     return requests.get('https://fr.openfoodfacts.org/api/v0/produit/' + str(self.barcode) + '.json').json()


class Component(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    # recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.FloatField()
#     ##TODO composite key
#
# class Recipe(models.Model):
#     name = models.CharField(max_length=255)
#     favorite = models.BooleanField()
