from django.urls import path
from . import views

urlpatterns = [
    path('parameters/', views.get_subject_number, name='get_subject_number'),
    path('intended_color/<int:number>/', views.intend_color, name='intended_color'),
]