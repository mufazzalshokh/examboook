from django.urls import path


# app_name = 'home'
from book.views import books_list

urlpatterns = [
    path('', books_list)
]
