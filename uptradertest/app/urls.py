from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name = 'test_url'),
    path('another/', views.index, name = 'ind'),
    path('third/', views.third, name = 'third')
]