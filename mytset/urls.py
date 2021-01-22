from django.urls import path

from .views import testFunc

urlpatterns = [
    path("", testFunc)
]