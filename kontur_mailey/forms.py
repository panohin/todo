from django import forms


class UploadFileForm(forms.Form):
	body = forms.CharField(max_length=250)
	theme = forms.CharField(max_length=250)
	file = forms.FileField()