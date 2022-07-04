from django.db import models

class Target(models.Model):
	name = models.CharField(max_length=254, verbose_name='Имя адресата')
		
	class Meta:
		verbose_name = 'Получатель рассылки'
		verbose_name_plural = 'Получатели рассылки'

	def __str__(self):
		return self.name


class FilterName(models.Model):
	name = models.CharField(
		max_length=254,
		verbose_name='Название фильтра',
		null=True
	)
	target = models.ForeignKey(
		Target,
		on_delete=models.SET_NULL,
		related_name='filters',
		null=True
	)
	need_to_send = models.BooleanField(default=False)

	class Meta:
		verbose_name = 'Фильтр'
		verbose_name_plural = 'Фильтры'

	def __str__(self):
		return self.name

class Emails(models.Model):
	email = models.EmailField(max_length=250)
	title = models.CharField(max_length=250, null=True)
	target = models.ForeignKey(
		Target,
		on_delete=models.SET_NULL,
		null=True,
		related_name='emails'
		)

	class Meta:
		verbose_name = 'Емэйл'
		verbose_name_plural = 'Емэйлы'

	def __str__(self):
		return self.email
