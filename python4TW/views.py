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
from python4TW.serializers import IngredientSerializer, UserSerializer
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User

def welcome(request):
    print("got to welcome")
    return HttpResponse("welcome to the API")



class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UserCreate(generics.CreateAPIView):
#     """
#     Creates the user.
#     """
#
#     def post(self, request, format='json'):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             if user:
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)

# def create_user(request):
#     serialized = UserSerializer(data=request.data)
#     if serialized.is_valid():
#         User.objects.create_user(
#             serialized.save()
#         )
#         return Response(serialized.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
