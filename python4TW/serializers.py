
from rest_framework import serializers
from python4TW.models import Ingredient, Component, Recipe
from django.contrib.auth.models import User
#
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('barcode', 'name','image','energy_100g','fat_100g','saturated_fat_100g', 'carbohydrates_100g','sugar_100g','protein_100g','salt_100g')
# #
class ComponentSerializer(serializers.ModelSerializer):
    recipe = serializers.PrimaryKeyRelatedField(many=False, queryset=Recipe.objects.all())
    class Meta:
        model = Component
        fields = ('ingredient','quantity', 'recipe')


class RecipeSerializer(serializers.ModelSerializer):
    components = serializers.PrimaryKeyRelatedField(many=True, queryset=Component.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Recipe
        fields = ('name','favorite', 'owner', 'components')

class UserSerializer(serializers.ModelSerializer):
    recipes = serializers.PrimaryKeyRelatedField(many=True, queryset=Recipe.objects.all())
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password','recipes')
