from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.cliente_list, name='cliente_list'),
    path('cliente/<int:pk>/', views.cliente_detail, name='cliente_detail'),
    path('cliente/new/', views.cliente_new, name='cliente_new'),
    path('cliente/<int:pk>/edit/', views.cliente_edit, name='cliente_edit'),
    path('cliente/<int:pk>/edit/', views.cliente_delete, name='cliente_delete'),    
]