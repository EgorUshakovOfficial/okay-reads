from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('', include('users.urls')),
    path('books/', include('book.urls')),
    path('admin/', admin.site.urls),
]
