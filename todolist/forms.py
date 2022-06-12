from django import forms

from .models import Tender

class TenderForm(forms.ModelForm):
	link = forms.URLField(label='Ссылка')

	class Meta:
		model = Tender
		fields = '__all__'

