from django.urls import path
from .views import index, sub01, sub02, sub03, sub04, sub05

from . import views

app_name = 'VPHI'

urlpatterns = [
    path('', index.main, name='index'),

    path('sub01/sub01_01', sub01.sub01_01, name='SUB01_01'),

    path('sub02/sub02_01', sub02.sub02_01, name='SUB02_01'),

    path('sub03/sub03_01', sub03.sub03_01, name='SUB03_01'),

    path('sub04/sub04_01', sub04.sub04_01, name='SUB04_01'),
    path('sub04/sub04_02', sub04.sub04_02, name='SUB04_02'),
    path('sub04/sub04_03', sub04.sub04_03, name='SUB04_03'),

    path('sub05/sub05_01', sub05.sub05_01, name='SUB05_01'),
]