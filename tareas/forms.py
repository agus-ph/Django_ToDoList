from django import forms
from django.forms import ModelForm

from .models import Tareas


class TareasForm(forms.ModelForm):
    titulo = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Agrega una nueva tarea..."})
    )

    class Meta:
        model = Tareas
        fields = "__all__"