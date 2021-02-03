from django import forms
from .models import *


class Userdetail(forms.ModelForm):
    class Meta:
        model = EmployeeDetail
        fields = ('name', 'email')
