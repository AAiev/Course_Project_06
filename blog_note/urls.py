from django.urls import path
from django.views.decorators.cache import never_cache

from blog_note.apps import BlogNoteConfig
from blog_note.views import BlogNoteCreateView, BlogNoteListView, BlogNoteDetailView, BlogNoteUpdateView, \
    BlogNoteDeleteView

app_name = BlogNoteConfig.name

urlpatterns = [
    path('create/', never_cache(BlogNoteCreateView.as_view()), name='create'),
    path('', BlogNoteListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogNoteDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', never_cache(BlogNoteUpdateView.as_view()), name='edit'),
    path('delete/<int:pk>/', BlogNoteDeleteView.as_view(), name='delete'),
]
