from django.urls import path
from .views import test

urlpatterns=[
    path('welcome', test, name='Hello')
]