from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('plan and pricing', views.services, name='index'),

    
]