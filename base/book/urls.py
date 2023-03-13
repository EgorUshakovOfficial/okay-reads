from django.urls import path
from .views import book_page, add_book, delete_book

urlpatterns = [
    path('<uuid:book_id>/', book_page, name='book_page'),
    path('new/', add_book, name='add_book'),
    path('delete/<uuid:book_id>/', delete_book, name="delete_book")
]