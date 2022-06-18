from django.urls import path
from . import views

urlpatterns = [
    path('parameters/', views.get_parameters_values, name='get_parameters_values'),
    path('solution/<str:a>/<str:b>/<str:c>/', views.get_solution, name='solution'),
]