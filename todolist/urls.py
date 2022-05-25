from django.urls import path

from .views import * 

urlpatterns = [
    path('', index, name='index_url'),
    path('todo/', todo, name='todolist_url'),
    path('add_tender/', add_tender, name='add_tender_url'),
    path('category/', category, name='category_url'),
]