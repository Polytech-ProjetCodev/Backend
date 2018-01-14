
from rest_framework import serializers
from python4TW.models import Ingredient, Component
from django.contrib.auth.models import User

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('barcode','name','energy_100g','fat_100g','saturated_fat_100g', 'carbohydrates_100g','sugar_100g','protein_100g','salt_100g')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')
