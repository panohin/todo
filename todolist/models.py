from django.db import models

class TenderCategory(models.Model):
	name = models.CharField(max_length=40)

	class Meta:
		verbose_name = 'Категория процедуры'
		verbose_name_plural = 'Категории процедур'

	def __str__(self):
		return self.name

class Department(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Currency(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Author(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Manager(models.Model):
	name = models.CharField(max_length=50, verbose_name='Имя менеджера')
	dept = models.ForeignKey(Department, on_delete = models.PROTECT)

	def __str__(self):
		return self.name

class Tender(models.Model):
	title = models.CharField(max_length=150, verbose_name='Название')
	created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
	author = models.ForeignKey(Author, on_delete=models.PROTECT, verbose_name='Сотрудник тендерного отдела')
	nominal_max_price = models.IntegerField(default=0, verbose_name='НМЦ')
	manager = models.ForeignKey(Manager, on_delete = models.PROTECT, verbose_name='Менеджер')
	review_status = models.BooleanField(null=True, blank=True, verbose_name='Статус рассмотрения')
	submit_date = models.DateTimeField(verbose_name='Дата подачи')
	process_date = models.DateTimeField(verbose_name='Дата процедуры')
	price = models.IntegerField(null=True ,blank=True, verbose_name='Цена участия')
	currency = models.ForeignKey(Currency, on_delete = models.PROTECT, verbose_name='Валюта')
	result = models.BooleanField(null=True, blank=True, verbose_name='Результат')
	comment = models.TextField(max_length=300, blank=True, verbose_name='Комментарий')
	importance = models.BooleanField(null=True, blank=True, verbose_name='Статус важности')
	link = models.CharField(max_length=200, blank=True, verbose_name='Ссылка')

	class Meta:
		ordering = ['-created_date']
		verbose_name = 'Закупочная процедура'
		verbose_name_plural = 'Закупочные процедуры'

	def __str__(self):
		return self.title

