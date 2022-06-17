from rest_framework import viewsets
from books.api import serealizers
from books import models

class BookViewset(viewsets.ModelViewSet):
    serializer_class = serealizers.BookSerealizer
    queryset = models.Book.objects.all()