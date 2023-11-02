from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework.utils import json
from .forms import userForm
from django.shortcuts import render


# Create your views here.


def index(request):
    response = request.get('http://127.0.0.1:8000/ingresoUsers/').json()
    return render(request, 'web/index.html', {
        'response': response
    })


def UsersPost(request):
    url = "http://127.0.0.1:8000/ingresoUsers/registro"
    form = userForm(request.POST or None)
    if form.is_valid():
        nombre = form.cleaned_data.get("nombre")
        apellido = form.cleaned_data.get("apellido")
        email = form.cleaned_data.get("email")
        tipoUsuario = form.cleaned_data.get("tipoUsuario")
        password = form.cleaned_data.get("password")
        data = {'nombre': nombre, 'apellido': apellido, 'email': email, 'tipoUsuario': tipoUsuario, 'password': password}
        headers = {'Content-type': 'application/json', }
        response = request.post(url, data=json.dumps(data), headers=headers)
        return render(request, 'web/form.html', {
            'response': response
        })