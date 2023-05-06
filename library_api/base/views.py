from django.shortcuts import render
from .forms import BookForm
from .models import Book

# Create your views here.

def home(request):
    books = Book.objects.all()
    return render(request, 'base/home.html', { 'books': books })

def search(request):
    return render(request, 'base/search.html')

def addBook(request):
    form = BookForm()
    return render(request, 'base/book.html', { 'form': form, 'script_filepath': '/static/js/add_book.js', 'method_type': 'POST' })

def updateBook(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)
    return render(request, 'base/book.html', { 'form': form, 'script_filepath': '/static/js/update_book.js', 'method_type': 'PATCH' })
