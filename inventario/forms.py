from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms

class productoForm(ModelForm):
    class Meta:
        model= producto
        fields = '__all__'