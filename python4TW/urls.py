from django.urls import path

from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

urlpatterns = [
    # url(r'^ingredient$', views.IngredientList, name='index'),
    path('', views.welcome),
    path('api-auth/', include('rest_framework.urls')),
    #
    # path('ingredient/', views.IngredientList.as_view()),
    # path('ingredient/<int:pk>/', views.IngredientDetail.as_view()),
    #
    path('recipe/', views.RecipeList.as_view()),
    path('recipe/<int:pk>/', views.RecipeDetail.as_view()),
    #
    # path('component/', views.ComponentList.as_view()),
    # path('component/<int:pk>/', views.ComponentDetail.as_view()),
    #
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/create/', views.UserCreate.as_view()),



    # path('component/', views.ComponentList)
    # url(r'^test/(?P<barcode>[0-9]{12})$', views.test, name="test"),
    # url(r'^testinsert/(?P<barcode>[0-9]{12})$', views.testinsert, name="testinsert")
]

urlpatterns = format_suffix_patterns(urlpatterns)
