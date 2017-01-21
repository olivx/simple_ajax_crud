from django.db import models
from django.shortcuts import resolve_url as r


class Books(models.Model):
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3
    BOOK_TYPES = (
        (HARDCOVER, 'Hardcover'),
        (PAPERBACK, 'Paperback'),
        (EBOOK, 'E-book'),
    )

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    publication_date = models.DateField(null=True)
    pages = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES)

    class Meta:
        ordering = ('title',)
        verbose_name = 'livro'
        verbose_name_plural = 'livros'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return r('book_update', pk=self.pk)
