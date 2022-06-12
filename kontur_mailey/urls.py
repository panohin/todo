from django.urls import path

from kontur_mailey.views import * 

urlpatterns = [
	path('', index),
    path('upload_kontur/', upload_kontur, name='upload_kontur_url'),
]