from django.urls import path

from kontur_mailey.views import * 

app_name = 'kontur_mailey'

urlpatterns = [
	path('', index, name='index_url'),
    path('upload_kontur/', upload_kontur, name='upload_kontur_url'),
]