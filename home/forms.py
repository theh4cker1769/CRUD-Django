from django import forms
from .models import User, Item

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'profileImg']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'profileImg': forms.FileInput(attrs={'class': 'form-control'}),
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['testName', 'testImage']
        widgets = {
            'testName': forms.TextInput(attrs={'class': 'form-control'}),
            'testImage': forms.FileInput(attrs={'class': 'form-control'}),
        }