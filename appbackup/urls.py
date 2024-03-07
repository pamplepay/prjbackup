from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dialog_add/', views.dialog_add, name='dialog_add'),
    path('save_pharmacy/', views.save_pharmacy, name='save_pharmacy'),
]
