
from rest_framework import serializers
from python4TW.models import Ingredient, Component

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('barcode','name','energy_100g','fat_100g','saturated_fat_100g', 'carbohydrates_100g','sugar_100g','protein_100g','salt_100g')
