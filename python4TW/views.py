# from django.shortcuts import render
# from django.http import HttpResponse
# from . import models
#
# # Create your views here.
#
#
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
#
#
#
# def test(request, barcode):
#     ingredient = models.Ingredient(barcode=barcode)
#     return HttpResponse(str(ingredient.get_information()))
#
#
# def testinsert(request, barcode):
#
#     ingredient = models.Ingredient(barcode=barcode)
#     # ingredient.get_information
#     print("ingrédient : ")
#     print(str(ingredient))
#     ingredient.save()

from python4TW.models import Ingredient
from python4TW.serializers import IngredientSerializer
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

def welcome(request):
    print("got to welcome")
    return HttpResponse("welcome to the API")



class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
