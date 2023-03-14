from django.urls import path
from .views import index, page_not_found

urlpatterns= [
    path('', index, name='index'),
    path('404/', page_not_found, name='not_found')
]