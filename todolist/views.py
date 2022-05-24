from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Tender

def redirect_view(request):
	return HttpResponse('redirect_view')

def todo(request):
	tenders = Tender.objects.all()
	return HttpResponse(tenders)

def category(request):
	return HttpResponse('category')