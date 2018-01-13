from django.urls import path

from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # url(r'^ingredient$', views.IngredientList, name='index'),
    path('', views.welcome),
    path('ingredient/', views.IngredientList.as_view()),
    path('ingredient/<int:pk>/', views.IngredientDetail.as_view())
    # path('component/', views.ComponentList)
    # url(r'^test/(?P<barcode>[0-9]{12})$', views.test, name="test"),
    # url(r'^testinsert/(?P<barcode>[0-9]{12})$', views.testinsert, name="testinsert")
]

urlpatterns = format_suffix_patterns(urlpatterns)
