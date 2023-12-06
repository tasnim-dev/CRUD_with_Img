from django.forms import ModelForm
from .models import Student
from django import forms


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'Student_name':forms.TextInput(attrs={'class':'form-control'}),
            'Department':forms.TextInput(attrs={'class':'form-control'}),
            'Phone':forms.TextInput(attrs={'class':'form-control'})
        }