from django.urls import path
from . import views

app_name = 'pizzas'
urlpatterns = [
#Домашняя страница
    path ('', views.index,name='index'),
    path ('pizzas/', views.pizzas,name='pizzas'),
    #Страница с подробной ипформацией по отдельной теме
	path('pizzas/<int:pizza_id>/',views.pizza,name='pizza'),
]
