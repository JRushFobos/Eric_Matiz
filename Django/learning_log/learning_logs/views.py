from django.shortcuts import render
from .models import Topic

def index(request):
    '''Домашняя страница приложения Learning Log'''
    return render (request, 'learning_logs/index.html')

def topics(request):
    #Выводим список тем
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    '''Вывод одну тему и все записи по ней'''
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set_order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render (request,'learning_logs/topic.html', context)