from django.db import models
from django.contrib.auht.models import User
# Create your models here.

class Allergen(models.Model):
    name = models.CharField(max_length=45)

class Ingredient(models.Model):
    barcode = models.CharField(max_length=13, primary_key=True)
    name = models.CharField(max_length=255)
    energy_100g = models.FloatField()
    fat_100g = models.FloatField()
    saturated_fat_100g = models.FloatField()
    glucid_100g = models.FloatField()
    sugar_100g = models.FloatField()
    protein_100g = models.FloatField()
    salt_100g = models.FloatField()


class Component(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.FloatField()
    ##TODO composite key

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    favorite = models.BooleanField()
