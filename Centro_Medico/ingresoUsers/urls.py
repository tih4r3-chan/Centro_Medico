from django.urls import path
from .import views

urlpatterns =[
    path('',views.listaUsers, name='listaUsers'),
    path('registro/',views.ingresoUser, name='ingresoUser'),
    path('eliminar/<str:pk>/',views.eliminarUser, name='eliminarUser'),
]