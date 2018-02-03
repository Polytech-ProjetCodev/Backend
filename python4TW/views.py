from python4TW.models import Ingredient, Component, Recipe
from python4TW.serializers import UserSerializer, RecipeSerializer, ComponentSerializer, IngredientSerializer
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import permissions
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
# from python4TW.permissions import IsOwnerOrReadOnly


def welcome(request):
    print("got to welcome")
    return HttpResponse("welcome to the API")


class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientDetail(APIView):
    serializer_class = IngredientSerializer

    def get_object(self, pk):
        try:
            return Ingredient.objects.get(pk=pk)
        except Ingredient.DoesNotExist:
            # on va le chercher dans openfoodfacts
            ingredient = Ingredient()

            try:
                ingredient.get_information(barcode=pk)
                return ingredient
            except KeyError:
                raise Http404
            except:
                print("Unexpected error")
                raise

    def get(self, request, pk, format=None):
        ingredient = self.get_object(pk)
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


class ComponentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer


class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


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
