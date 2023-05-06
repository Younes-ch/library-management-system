from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'publishing_year', 'pages', 'chapters']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'search-bar-input', 'required': True}),
            'author': forms.TextInput(attrs={'class': 'search-bar-input', 'required': True}),
            'genre': forms.TextInput(attrs={'class': 'search-bar-input', 'required': True}),
            'publishing_year': forms.NumberInput(attrs={'class': 'search-bar-input', 'required': True}),
            'pages': forms.NumberInput(attrs={'class': 'search-bar-input', 'required': True}),
            'chapters': forms.NumberInput(attrs={'class': 'search-bar-input', 'required': True}),
        }
