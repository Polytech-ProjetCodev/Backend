
from rest_framework import serializers
from python4TW.models import Ingredient, Component, Recipe
from django.contrib.auth.models import User
#
# class IngredientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ingredient
#         fields = ('barcode','name','energy_100g','fat_100g','saturated_fat_100g', 'carbohydrates_100g','sugar_100g','protein_100g','salt_100g')
# #
# class ComponentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Component
#         fields = ('ingredient','quantity', 'recipe')
#

class RecipeSerializer(serializers.ModelSerializer):
    # components = serializers.PrimaryKeyRelatedField(many=True, queryset=Component.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Recipe
        # fields = ('name','favorite', 'components','owner')
        fields = ('name','favorite', 'owner')

class UserSerializer(serializers.ModelSerializer):
    recipes = serializers.PrimaryKeyRelatedField(many=True, queryset=Recipe.objects.all())
    class Meta:
        model = User
        # fields = ('id', 'email', 'username', 'password')
        fields = ('id', 'email', 'username', 'password','recipes')
