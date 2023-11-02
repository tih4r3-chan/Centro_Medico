from django import forms


class userForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    tipoUsuario = forms.CharField(max_length=60)
    password = forms.CharField(max_length=100)