from django import forms
from .models import Worker

class WorkerForm(forms.ModelForm):
    model= Worker
    fields = '__all__'


