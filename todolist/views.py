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

def update_tender(request, tender_id):
	title = 'Редактирование тендера'
	if request.POST:
		bound_form = TenderForm(request.POST)
		if bound_form.errors:
			return render(request, 'todolist/update_tender.html', context={'form':bound_form, 'title':title})
		else:
			if bound_form.is_valid():
				tender = Tender.objects.filter(pk=tender_id).update(**bound_form.cleaned_data)
				return redirect('todolist:index_url')
	else:
		tender = Tender.objects.get(pk=tender_id)
		form = TenderForm(instance=tender)
		return render(request, 'todolist/update_tender.html', context={'title':title, 'form':form, 'tender':tender})


def todo(request):
	tenders = Tender.objects.all()
	title = ''
	context = {'title':title}
	return render(request, 'todolist/todo.html')

def category(request):
	return HttpResponse('category')

