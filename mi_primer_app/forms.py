# mi_primer_app/forms.py

from django import forms
from .models import Curso


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'camada']
