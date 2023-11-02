from django.urls import path
from .views import Ingreso

urlpatterns =[
    path('ingreso/',Ingreso.as_view(), name='lista_users')
]