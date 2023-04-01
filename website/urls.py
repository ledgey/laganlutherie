# project/urls.py

from django.urls import include, path

urlpatterns = [
    path('', include('LaganLutherie.urls')),
]

