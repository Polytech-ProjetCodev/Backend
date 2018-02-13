from rest_framework import serializers
from python4TW.models import Ingredient, Component, Recipe
from django.contrib.auth.models import User


class IngredientSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    image = serializers.CharField(read_only=True)
    energy_100g = serializers.FloatField(read_only=True)
    fat_100g = serializers.FloatField(read_only=True)
    saturated_fat_100g = serializers.FloatField(read_only=True)
    carbohydrates_100g = serializers.FloatField(read_only=True)
    sugar_100g = serializers.FloatField(read_only=True)
    protein_100g = serializers.FloatField(read_only=True)
    salt_100g = serializers.FloatField(read_only=True)

    class Meta:
        model = Ingredient
        fields = '__all__'

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        # fields='__all__'
        fields = ['ingredient', 'quantity']


class RecipeSerializer(serializers.ModelSerializer):
    components = ComponentSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    energy = serializers.FloatField(read_only=True, default=0)
    fat = serializers.FloatField(read_only=True, default=0)
    saturated = serializers.FloatField(read_only=True, default=0)
    carbohydrates = serializers.FloatField(read_only=True, default=0)
    sugar = serializers.FloatField(read_only=True, default=0)
    protein = serializers.FloatField(read_only=True, default=0)
    salt = serializers.FloatField(read_only=True, default=0)

    class Meta:
        model = Recipe
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True, read_only=True)


    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'recipes')
