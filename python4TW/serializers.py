
from rest_framework import serializers
from python4TW.models import Ingredient, Component, Recipe
from django.contrib.auth.models import User
#


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class ComponentSerializer(serializers.ModelSerializer):
    # recipe = serializers.PrimaryKeyRelatedField(many=False, queryset=Recipe.objects.all())
    ingredient = IngredientSerializer()

    class Meta:
        model = Component
        exclude = ['recipe']

    # def create(self, validated_data):
    #     pass


class RecipeSerializer(serializers.ModelSerializer):
    components = ComponentSerializer(many=True)
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
    recipes = RecipeSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'recipes')
