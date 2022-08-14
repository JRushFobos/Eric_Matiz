from django.db import models


# Create your models here.
class Pizza(models.Model):
    #'''Описание модели Pizza наследованной из models.Model'''
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    #'''Возвращает строковое представление модели'''
        return self.name


class Topping(models.Model):
    #'''Описание модели Topping наследованной из models.Model'''
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'toppings'
    
    def __str__(self):
    #'''Возвращает строковое представление модели'''
        return self.name