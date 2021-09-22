from django.shortcuts import render

from book.models import BookModel


def books_list(request):
    books = BookModel.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books_list.html', context)

