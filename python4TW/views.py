from python4TW.models import Ingredient, Component, Recipe
from python4TW.serializers import UserSerializer, RecipeSerializer, ComponentSerializer, IngredientSerializer
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
# from rest_framework import permissions
from rest_framework import mixins

from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
# from python4TW.permissions import IsOwnerOrReadOnly


def welcome(request):
    print("got to welcome")
    return HttpResponse("welcome to the API")


class IngredientList(generics.ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientDetail(APIView):
    serializer_class = IngredientSerializer

    def get_object(self, pk):
        try:
            return Ingredient.objects.get(pk=pk)
        except Ingredient.DoesNotExist:
            print("l'ingrédient n'existe pas")
            # on va le chercher dans openfoodfacts
            ingredient = Ingredient()

            try:
                ingredient.get_information(barcode=pk)
                ingredient.save()
                return ingredient
            except KeyError:
                raise Http404
            except:
                print("Unexpected error")
                raise

    def get(self, request, pk, format=None):
        ingredient = self.get_object(pk)
        ingredient.save();
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ingredient = self.get_object(pk)
        serializer = IngredientSerializer(ingredient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ingredient = self.get_object(pk)
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ComponentList(generics.ListCreateAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

    def perform_create(self, serializer):
        serializer.save()
        recipe = Recipe.objects.get(pk=serializer.data.get('recipe'))
        quantity = serializer.data.get('quantity')
        ingredient = Ingredient.objects.get(barcode=serializer.data.get('ingredient'))

        #updating the recipe's nutritional values based on the quantity of the ingredient added 
        recipe.energy += ingredient.energy_100g*quantity/100
        recipe.fat += ingredient.fat_100g*quantity/100
        recipe.saturated += ingredient.saturated_fat_100g*quantity/100
        recipe.carbohydrates += ingredient.carbohydrates_100g*quantity/100
        recipe.sugar += ingredient.sugar_100g*quantity/100
        recipe.protein += ingredient.protein_100g*quantity/100
        recipe.salt += ingredient.salt_100g*quantity/100

        recipe.save()
    


class ComponentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

    def perform_update(self, serializer):
        serializer.save()

        recipe = serializer.validated_data.get('recipe')
        recipe_components = Component.objects.filter(recipe=recipe)

        recipe.energy = 0
        recipe.fat = 0
        recipe.saturated = 0
        recipe.carbohydrates = 0
        recipe.sugar = 0
        recipe.protein = 0
        recipe.salt = 0
        for component in recipe_components:
            ingredient = component.ingredient
            quantity = component.quantity
            recipe.energy = ingredient.energy_100g*quantity/100
            recipe.fat = ingredient.fat_100g*quantity/100
            recipe.saturated = ingredient.saturated_fat_100g*quantity/100
            recipe.carbohydrates = ingredient.carbohydrates_100g*quantity/100
            recipe.sugar = ingredient.sugar_100g*quantity/100
            recipe.protein = ingredient.protein_100g*quantity/100
            recipe.salt = ingredient.salt_100g*quantity/100
            
        recipe.save()






    def perform_destroy(self, instance):
        ingredient = instance.ingredient
        recipe = instance.recipe
        quantity = instance.quantity

        print(ingredient)
        print(recipe)
        print(quantity)

        print(ingredient.energy_100g*quantity/100)
        recipe.energy -= ingredient.energy_100g*quantity/100
        recipe.fat -= ingredient.fat_100g*quantity/100
        recipe.saturated -= ingredient.saturated_fat_100g*quantity/100
        recipe.carbohydrates -= ingredient.carbohydrates_100g*quantity/100
        recipe.sugar -= ingredient.sugar_100g*quantity/100
        recipe.protein -= ingredient.protein_100g*quantity/100
        recipe.salt -= ingredient.salt_100g*quantity/100

        recipe.save()
        instance.delete()

class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def perform_create(self, serializer):
        # serializer.save(owner=self.request.user)
        serializer.save(owner=User.objects.get(id='1'))


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
