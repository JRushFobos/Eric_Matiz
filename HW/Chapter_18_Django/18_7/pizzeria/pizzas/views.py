from django.shortcuts import render
from .models import Pizza

def index(request):
	return render (request, 'pizzas/index.html')

def pizzas(request):
   	#Выводим список тем
	pizzas = Pizza.objects.order_by('date_added')
	context = {'pizzas':pizzas}
	return render(request, 'pizzas/pizzas.html', context)

#def pizza из view.py должна получить тему и записи из базы
def pizza(request, pizza_id):   #pizza_id еще один параметр
    '''Вывод одну тему и все записи по ней'''
    pizza = Pizza.objects.get(id=pizza_id)									#get для получаения темы
    toppings = pizza.topping_set.order_by('-date_added')#загружаем записи в обр порядке
    context = {'pizza':pizza,'toppings':toppings} #тема и записи сохр в list context
    return render (request,'pizzas/pizza.html', context) #list context передается в topic.html