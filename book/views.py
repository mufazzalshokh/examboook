from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from book.models import BookModel


class BookListView(LoginRequiredMixin, ListView):
    template_name = 'books_list.html'
    model = BookModel
    queryset = BookModel.objects.order_by('-pk')
