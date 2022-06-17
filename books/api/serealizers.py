from rest_framework import serializers
from books import models

class BookSerealizer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'