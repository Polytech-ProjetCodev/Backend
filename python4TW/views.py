from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



def test(request, barcode):
    ingredient = models.Ingredient(barcode=barcode)
    return HttpResponse(str(ingredient.get_information()))


def testinsert(request, barcode):

    ingredient = models.Ingredient(barcode=barcode)
    # ingredient.get_information
    print("ingrédient : ")
    print(str(ingredient))
    ingredient.save()
