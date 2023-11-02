from django.shortcuts import render
from django.views import View
from .models import Users
from django.http.response import JsonResponse

# vista basada en la clase 
class Ingreso(View):
    # metodo post
    def get(self, request):
        usuarios = list(Users.objects.values())
        if len(usuarios)>0:
            datos={'message': "Exitoso",'usuarios': usuarios}
        else:
            datos={'message': "No se encontraron usuarios :("}
        return JsonResponse(datos)
    
    def POST(self, request):
        pass
    
    def DELETE(self, request):
        pass