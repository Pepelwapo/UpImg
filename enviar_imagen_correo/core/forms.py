# core/forms.py

from django import forms
from .models import ImageEmail

class ImageEmailForm(forms.ModelForm):
    class Meta:
        model = ImageEmail
        fields = ['email', 'image']
