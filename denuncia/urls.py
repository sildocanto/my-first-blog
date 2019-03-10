from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.cliente_intro, name='cliente_intro'),
    path('cliente/list/', views.cliente_list, name='cliente_list'),
    path('cliente/<int:pk>/', views.cliente_detail, name='cliente_detail'),
    path('cliente/new/', views.cliente_new, name='cliente_new'),
    path('cliente/<int:pk>/edit/', views.cliente_edit, name='cliente_edit'),
<<<<<<< HEAD
    path('cliente/<int:pk>/del/', views.cliente_delete, name='cliente_delete'),   
=======
    path('cliente/<int:pk>/del/', views.cliente_delete, name='cliente_delete'),

    path('estado/', views.estado_list, name='estado_list'),
    path('estado/<int:pk>/', views.estado_detail, name='estado_detail'),
    path('estado/new/', views.estado_new, name='estado_new'),
    path('estado/<int:pk>/edit/', views.estado_edit, name='estado_edit'),
    path('estado/<int:pk>/del/', views.estado_delete, name='estado_delete'), 

    path('vehiculo/', views.vehiculo_list, name='vehiculo_list'),
    path('vehiculo/<str:pk>/', views.vehiculo_detail, name='vehiculo_detail'),
    path('vehiculo/new/', views.vehiculo_new, name='vehiculo_new'),
    path('vehiculo/<str:pk>/edit/', views.vehiculo_edit, name='vehiculo_edit'),
    path('vehiculo/<str:pk>/del/', views.vehiculo_delete, name='vehiculo_delete'),


    path('incidente/', views.incidente_list, name='incidente_list'),
    path('incidente/<int:pk>/', views.incidente_detail, name='incidente_detail'),
    path('incidente/new/', views.incidente_new, name='incidente_new'),
    path('incidente/<int:pk>/edit/', views.incidente_edit, name='incidente_edit'),
    path('incidente/<int:pk>/del/', views.incidente_delete, name='incidente_delete'),


    path('poliza/', views.poliza_list, name='poliza_list'),
    path('poliza/<str:pk>/', views.poliza_detail, name='poliza_detail'),  
    path('poliza/new/', views.poliza_new, name='poliza_new'),
    path('poliza/<str:pk>/edit/', views.poliza_edit, name='poliza_edit'),
    path('poliza<str:pk>/del/', views.poliza_delete, name='poliza_delete'),


    path('usuario/', views.usuario_list, name='usuario_list'),
    path('usuario/<int:pk>/', views.usuario_detail, name='usuario_detail'),
    path('usuario/new/', views.usuario_new, name='usuario_new'),
    path('usuario/<int:pk>/edit/', views.usuario_edit, name='usuario_edit'),
    path('usuario<int:pk>/del/', views.usuario_delete, name='usuario_delete'),

    path('archivo/', views.archivo_list, name='archivo_list'),
    path('archivo/<int:pk>/', views.archivo_detail, name='archivo_detail'),
    path('archivo/new/', views.archivo_new, name='archivo_new'),
    path('archivo/<int:pk>/edit/', views.archivo_edit, name='archivo_edit'),
    path('archivo/<int:pk>/del/', views.archivo_delete, name='archivo_delete'),

    path('comentario/', views.comentario_list, name='comentario_list'),
    path('comentario/<int:pk>/', views.comentario_detail, name='comentario_detail'),
    path('comentario/new/', views.comentario_new, name='comentario_new'),
    path('comentario/<int:pk>/edit/', views.comentario_edit, name='comentario_edit'),
    path('comentario/<int:pk>/del/', views.comentario_delete, name='comentario_delete'),
   
>>>>>>> eed97789f87c7b6aa94e8eac792c8d2f8cd9f672
]