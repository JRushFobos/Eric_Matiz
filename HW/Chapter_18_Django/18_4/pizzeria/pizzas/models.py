from django.db import models


# Create your models here.
class Pizza(models.Model):
    '''�������� ������ ���� ��᫥����� �� models.Model'''
    name = models.CharField(max_length=200)

    def __str__(self):
    #'''�����頥� ��ப���� �।�⠢����� ������'''
        return self.name


class Topping(models.Model):
    '''�������� ������ ⮯���� ��᫥����� �� models.Model'''
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
    #'''�����頥� ��ப���� �।�⠢����� ������'''
        return self.name