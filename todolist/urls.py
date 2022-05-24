from django.urls import path

from .views import * 

urlpatterns = [
    path('', redirect_view),
    path('todo/', todo, name='todolist_url'),
    path('category/', category, name='category_url'),
]