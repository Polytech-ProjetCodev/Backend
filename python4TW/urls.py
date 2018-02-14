from django.urls import path
from rest_framework.authtoken import views as drf_auth_views

from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

urlpatterns = [
    path('', views.welcome),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', drf_auth_views.obtain_auth_token),


    path('ingredient/', views.IngredientList.as_view()),
    path('ingredient/<int:pk>/', views.IngredientDetail.as_view()),

    path('recipe/', views.RecipeList.as_view()),
    path('recipe/<int:pk>/', views.RecipeDetail.as_view()),

    path('component/', views.ComponentList.as_view()),
    path('component/<int:pk>/', views.ComponentDetail.as_view()),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/create/', views.UserCreate.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
