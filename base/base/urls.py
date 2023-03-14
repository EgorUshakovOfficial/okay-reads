from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.main.urls')),
    path('', include('apps.users.urls')),
    path('books/', include('apps.book.urls')),
    path('admin/', admin.site.urls),
]
