from django.db import models

class Target(models.Model):
	name = models.CharField(max_length=254, verbose_name='Имя адресата')
		
	class Meta:
		verbose_name = 'Получатель рассылки'
		verbose_name_plural = 'Получатели рассылки'

	def __str__(self):
		return self.name


class FilterName(models.Model):
	name = models.CharField(max_length=254, verbose_name='Название фильтра')
	target = models.ForeignKey(
		Target,
		on_delete=models.SET_NULL,
		related_name='filters', null=True
		)
	need_to_send = models.BooleanField(default=False)

	class Meta:
		verbose_name = 'Фильтр'
		verbose_name_plural = 'Фильтры'

	def __str__(self):
		return self.name

class Emails(models.Model):
	email = models.EmailField(max_length=250)
	target = models.ForeignKey(
		Target,
		on_delete=models.SET_NULL,
		null=True,
		related_name='emails'
		)
