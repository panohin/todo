from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Tender

def index(request):
	title = 'Главная'
	context = {'title':title}
	return render(request, 'todolist/main.html', context=context)


def todo(request):
	tenders = Tender.objects.all()
	title = ''
	context = {'title':}
	return render(request, 'todolist/todo.html')

def category(request):
	return HttpResponse('category')