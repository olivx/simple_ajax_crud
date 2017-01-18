from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from core import views as views_core


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^books/$', views_core.book_list, name='book_list'),
    url(r'^books/create/$', views_core.book_create, name='book_create'),
    url(r'^books/update/(?P<pk>\d+)/$',
        views_core.book_update, name='book_update'),
    url(r'^books/delete/(?P<pk>\d+)/$',
        views_core.book_delete, name='book_delete'),
    url(r'^admin/', admin.site.urls),
]
