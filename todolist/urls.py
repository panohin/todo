from django.urls import path

from .views import * 


app_name = 'todolist'

urlpatterns = [
    path('', index, name='index_url'),
    path('delete_tender/<int:tender_id>/', delete_tender, name='delete_tender_url'),
    path('update_tender/<int:tender_id>', update_tender, name='update_tender_url'),
    path('todo/', todo, name='todolist_url'),
    path('add_tender/', add_tender, name='add_tender_url'),
    path('category/', category, name='category_url'),
]