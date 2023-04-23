from rest_framework.serializers import ModelSerializer
from base.models import Book

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
