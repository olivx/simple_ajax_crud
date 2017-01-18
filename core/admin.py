from django.contrib import admin
from .models import Books
from .forms import BookForms


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'author', 'publication_date',
                    'pages', 'price')
    search_fields = ('title', 'author',)
    list_filter = ('book_type',)

    form = BookForms
