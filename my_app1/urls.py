from django.urls import path

from my_app1 import views

urlpatterns = [
    path('', views.index, name='index')
]