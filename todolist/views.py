from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import NON_FIELD_ERRORS

from .models import Tender
from .forms import TenderForm

def index(request):
	title = 'Главная'
	tenders = Tender.objects.all()
	context = {'title': title, 'tenders': tenders}
	return render(request, 'todolist/main.html', context=context)

def add_tender(request):
	title = 'Добавить тендер'
	if request.POST:
		tender = TenderForm(request.POST)
		if tender.errors:
			return render(request, 'todolist/add_tender.html', context={'form':tender, 'title':title})
		else:
			if tender.is_valid():
				tender.save()
				return redirect('index_url')
	else:
		form = TenderForm()
		return render(request, 'todolist/add_tender.html', context={'form':form, 'title':title})

def delete_tender(request, tender_id):
	Tender.objects.filter(pk=tender_id).delete()
	return redirect('index_url')



def todo(request):
	tenders = Tender.objects.all()
	title = ''
	context = {'title':title}
	return render(request, 'todolist/todo.html')

def category(request):
	return HttpResponse('category')