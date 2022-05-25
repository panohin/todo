from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Tender
from .forms import TenderForm

def index(request):
	title = 'Главная'
	tenders = Tender.objects.all()
	context = {'title': title, 'tenders': tenders}
	return render(request, 'todolist/main.html', context=context)

def add_tender(request):
	form = TenderForm()
	title = 'Добавить тендер'
	return render(request, 'todolist/add_tender.html', context={'form':form, 'title':title})

def todo(request):
	tenders = Tender.objects.all()
	title = ''
	context = {'title':title}
	return render(request, 'todolist/todo.html')

def category(request):
	return HttpResponse('category')