from django.db import models


# Create your models here.
class Pizza(models.Model):
    '''Создание модели пицца наследуется от models.Model'''
    name = models.CharField(max_length=200)

    def __str__(self):
    #'''Возвращает строковое представление модели'''
        return self.name


class Topping(models.Model):
    '''Создание модели топпинг наследуется от models.Model'''
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
    #'''Возвращает строковое представление модели'''
        return self.name