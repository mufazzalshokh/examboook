from django.db import models


class AuthorModel(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class CategoryModel(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class BookModel(models.Model):
    title = models.CharField(max_length=50)
    page_count = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(AuthorModel,
                               on_delete=models.CASCADE,
                               related_name='books')
    category = models.ForeignKey(CategoryModel,
                                 on_delete=models.PROTECT,
                                 related_name='books', null=True)
    # cover = models.ImageField(upload_to='cover')
    # is_booked = models.BooleanField(default=False)
    # booked_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'


class UserModel(models.Model):
    user = models.OneToOneField(BookModel, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
