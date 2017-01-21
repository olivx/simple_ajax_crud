from django import forms
from .models import Books


class BookForms(forms.ModelForm):

    class Meta:
        model = Books
        fields = ('title', 'author', 'publication_date',
                  'pages', 'price', 'book_type',)
