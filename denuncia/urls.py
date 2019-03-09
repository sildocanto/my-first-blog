from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.cliente_list, name='cliente_list'),
    path('cliente/<int:pk>/', views.cliente_detail, name='cliente_detail'),
    path('cliente/new/', views.cliente_new, name='cliente_new'),
    path('cliente/<int:pk>/edit/', views.cliente_edit, name='cliente_edit'),
    path('cliente/<int:pk>/edit/', views.cliente_delete, name='cliente_delete'),

    path('estado/', views.estado_list, name='estado_list'),
    path('estado/<int:pk>/', views.estado_detail, name='estado_detail'),
    path('estado/new/', views.estado_new, name='estado_new'),
    path('estado/<int:pk>/edit/', views.estado_edit, name='estado_edit'),
    path('estado/<int:pk>/edit/', views.estado_delete, name='estado_delete'), 

    path('vehiculo/', views.vehiculo_list, name='vehiculo_list'),
    path('vehiculo/<int:pk>/', views.vehiculo_detail, name='vehiculo_detail'),
    path('vehiculo/new/', views.vehiculo_new, name='vehiculo_new'),
    path('vehiculo/<int:pk>/edit/', views.vehiculo_edit, name='vehiculo_edit'),
    path('vehiculo/<int:pk>/edit/', views.vehiculo_delete, name='vehiculo_delete'),
   
]