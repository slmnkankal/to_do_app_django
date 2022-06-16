from importlib.metadata import files
from pyexpat import model
from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"