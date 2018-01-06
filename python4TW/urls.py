from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test/(?P<barcode>[0-9]{12})$', views.test, name="test"),
    url(r'^testinsert/(?P<barcode>[0-9]{12})$', views.testinsert, name="testinsert")
]
