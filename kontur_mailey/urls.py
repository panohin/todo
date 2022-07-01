from django.urls import path

from kontur_mailey.views import * 

app_name = 'kontur_mailey'

urlpatterns = [
	path('', upload_kontur, name='upload_kontur_url'),
]