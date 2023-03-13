from django.contrib import admin
from .models import Book, Review

# Register Book and Review models
admin.site.register(Review)
admin.site.register(Book)
