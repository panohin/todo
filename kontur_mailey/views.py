from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import UploadFileForm
from . import services



def upload_kontur(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			services.handle_uploaded_file(request.FILES.get('file'))
		return redirect('/')
	else:
		form = UploadFileForm()
		title = 'Загрузка файла Контур.Закупок'
		context = {'title':title, 'form':form}
		return render(request, 'kontur_mailey/upload_kontur.html', context=context)

