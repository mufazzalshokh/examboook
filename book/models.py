from django.contrib.auth.backends import UserModel
from django.db import models


class BookModel(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='cover', null=True)
    is_booked = models.BooleanField(default=False)
    booked_by = models.ForeignKey(UserModel, models.PROTECT, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'


class UserModel(models.Model):
    user = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='image')
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
