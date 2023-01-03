from django.db import forms



class BuscarCarro(forms.Form):
    nombre = forms.CharField(max_length=100)