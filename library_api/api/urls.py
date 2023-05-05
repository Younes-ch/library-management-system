from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('getAllYears/', views.getAllYears),
    path('books/', views.getBooks),
    path('books/<int:pk>/', views.getBook),
    path('books/search/title/<str:title>/', views.searchBooksByTitle),
    path('books/search/author/<str:author>/', views.searchBooksByAuthor),
    path('books/search/genre/<str:genre>/', views.searchBooksByGenre),
    path('books/search/year/<int:year>/', views.searchBooksByYear),
    path('books/add/', views.addBook),
    path('books/update/<int:pk>/', views.updateBook),
    path('books/delete/<int:pk>/', views.deleteBook),
    path('books/delete/all/', views.deleteAllBooks),
]