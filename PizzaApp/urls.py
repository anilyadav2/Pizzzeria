
from django.urls import path
from . import views
app_name='PizzaApp'
urlpatterns = [
    path('', views.index, name='index'),
    ]




