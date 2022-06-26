from django.http import HttpResponse
from django.shortcuts import render

from .forms import UploadFileForm


def upload_kontur(request):
	if request.POST:
		return redirect('index_url')
	else:
		form = UploadFileForm()
		title = 'Загрузка файла Контур.Закупок'
		context = {'title':title, 'form':form}
		return render(request, 'kontur_mailey/upload_kontur.html', context=context)

def index(request):
	return HttpResponse('<h3>Приложение KONTUR MAILEY</h3>')