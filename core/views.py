from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from core.models import Books
from core.forms import BookForms


def book_list(request):
    books = Books.objects.all()
    return render(request, 'book_list.html', {'book_list': books})


def book_create_form(request, form, template_name):
    data = {}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            books = Books.objects.all()
            data['html_book_list'] = render_to_string(
                'includes/partial_book_list.html', {'book_list': books})
            data['is_form_valid'] = True
        else:
            data['is_form_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)

    return JsonResponse(data)


def book_create(request):
    if request.method == 'POST':
        form = BookForms(request.POST)
    else:
        form = BookForms()

    return book_create_form(request, form, 'includes/partial_book_create.html')


def book_update(request, pk):
    book = get_object_or_404(Books, pk=pk)

    if request.method == 'POST':
        form = BookForms(request.POST, instance=book)
    else:
        form = BookForms(instance=book)

    return book_create_form(request, form, 'includes/partial_book_update.html')


def book_delete(request, pk):
    data = {}
    book = get_object_or_404(Books, pk=pk)

    if request.method == 'POST':
        book.delete()
        books = Books.objects.all()
        data['is_form_valid'] = True
        data['html_book_list'] = render_to_string(
            'includes/partial_book_list.html', {'book_list': books})
    else:
        data['is_form_valid'] = False
        context = {'book': book}
        data['html_form'] = render_to_string(
            'includes/partial_book_delete.html', context, request=request)

    return JsonResponse(data)
