from django.urls import path
from . import views

app_name = 'data_menu'

urlpatterns = [
    path('', views.index, name='index'),
]