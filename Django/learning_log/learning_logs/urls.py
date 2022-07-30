#Определение схемы URL для learning_logs
from django.urls import path
from . import views

app_name = 'leaning_logs'
urlpatterns = [
    #Домашняя страница
    path ('',vews.index, name='index')
]