from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from base.models import Book
from rest_framework import status

def get_book_url_and_cover(title):
    import requests

    url = f"https://hapi-books.p.rapidapi.com/search/{title}"

    headers = {
        "content-type": "application/octet-stream",
        "X-RapidAPI-Key": "ec2f8ccf8bmshbf1cf334816d19ep12966ejsnbf378abe0c43",
        "X-RapidAPI-Host": "hapi-books.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    json_data = response.json()
    
    return json_data

# Create your views here.
@api_view(['GET'])
def index(request):
    routes = [
        'api/getAllYears/',
        'api/books/',
        'api/books/<book_id>/',
        'api/books/add/',
        'api/books/update/<book_id>/',
        'api/books/delete/<book_id>/',
        'api/books/delete/all/',
        'api/books/search/title/<title>/',
        'api/books/search/author/<author>/',
        'api/books/search/genre/<genre>/',
        'api/books/search/year/<year>/',
    ]
    return Response(routes)

@api_view(['GET'])
def getAllYears(request):
    books = Book.objects.all()
    years = []
    for book in books:
        years.append(book.publishing_year)
    years = list(set(years))
    years.sort()
    return Response(years)

@api_view(['GET'])
def getBooks(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    if books:
        return Response(serializer.data)
    else:
        return Response({'message': 'No books found.'})

@api_view(['GET'])
def getBook(request, pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def searchBooksByTitle(request, title):
    books = Book.objects.filter(title__icontains=title)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def searchBooksByAuthor(request, author):
    books = Book.objects.filter(author__icontains=author)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def searchBooksByGenre(request, genre):
    books = Book.objects.filter(genre__icontains=genre)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def searchBooksByYear(request, year):
    books = Book.objects.filter(publishing_year=year)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addBook(request):
    data = request.data
    if isinstance(data, list):
        serializer = BookSerializer(data=data, many=True)
    else:
        serializer = BookSerializer(data=data)
    if serializer.is_valid():
        if isinstance(data, list):
            temp = []
            for book in serializer.validated_data:
                if Book.objects.filter(title=book['title']):
                    temp.append({
                                    'title': book['title'],
                                    'message': 'Book already exists.',
                                })
                else:
                    json_data = get_book_url_and_cover(book['title'])
                    if json_data:
                        try:
                            book['link'] = json_data[0].get('url', None)
                            book['cover'] = json_data[0].get('cover', None)
                        except:
                            book['link'] = None
                            book['cover'] = None
                    temp.append(book)
                    serializer = BookSerializer(data=temp[-1], many=False)
                    if serializer.is_valid():
                        serializer.save()
            return Response(temp)
        else:
            if Book.objects.filter(title=serializer.validated_data['title']):
                return Response({'message': 'Book already exists.'})
            json_data = get_book_url_and_cover(serializer.validated_data['title'])
            if json_data:
                serializer.save(link=json_data[0].get('url', None), cover=json_data[0].get('cover', None))
                return Response(serializer.data)
        serializer.save()
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data)

@api_view(['PATCH'])
def updateBook(request, pk):    
    data = request.data
    try:
        book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        return Response({'message': 'Book does not exist.'})
    serializer = BookSerializer(instance=book, data=data, partial=True)
    if serializer.is_valid(): 
        if serializer.validated_data.get('title', None):
            if book.title != serializer.validated_data['title']:
                if Book.objects.filter(title=serializer.validated_data['title']):
                    return Response({'message': 'Book already exists.'})
            json_data = get_book_url_and_cover(serializer.validated_data['title'])
            if json_data:
                serializer.save(link=json_data[0].get('url', None), cover=json_data[0].get('cover', None))
        serializer.save()
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data)  

@api_view(['DELETE'])
def deleteBook(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return Response({ 'message': 'Book deleted' })

@api_view(['DELETE'])
def deleteAllBooks(request):
    books = Book.objects.all()
    books.delete()
    return Response({ 'message': 'All books deleted' })
