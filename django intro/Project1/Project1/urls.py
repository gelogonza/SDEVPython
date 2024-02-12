from django.contrib import admin
from django.urls import path, include
from myapp.views import book_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('myapp.urls')),
    path('', book_list, name='root'),
]
