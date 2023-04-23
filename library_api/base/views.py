from django.shortcuts import render
from .models import Book

# Create your views here.

def home(request):
    books = Book.objects.all()
    return render(request, 'base/home.html', { 'books': books })

def search(request):
    return render(request, 'base/search.html')

def addBook(request):
    return render(request, 'base/add_book.html')
