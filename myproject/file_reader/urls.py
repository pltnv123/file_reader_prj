from django.urls import path
from . import views

urlpatterns = [
    path('', views.wordcount, name='wordcount'),
    path('clear-memory/', views.clear_memory, name='clear_memory'),
]