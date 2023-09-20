from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify


from blog_note.models import Blog_note


class BlogNoteCreateView(CreateView):
    model = Blog_note
    fields = ('title', 'content', 'image', 'sign_of_publication', 'slug',)
    success_url = reverse_lazy('blog_note:list')

    def form_valid(self, form):
        if form.is_valid():
            new_slug = form.save()
            new_slug.slug = slugify(new_slug.title)
            new_slug.save()

        return super().form_valid(form)

class BlogNoteListView(ListView):
    model = Blog_note

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(sign_of_publication=True)
        return queryset


class BlogNoteDetailView(DetailView):
    model = Blog_note

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.quantity_views += 1
        self.object.save()
        return self.object

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        blog_note_item = Blog_note.objects.get(pk=self.kwargs.get('pk'))
        context_data['pk'] = blog_note_item.pk
        context_data['title'] = blog_note_item.title
        return context_data

class BlogNoteUpdateView(UpdateView):
    model = Blog_note
    fields = ('title', 'content', 'image', 'sign_of_publication', 'slug',)
    # success_url = reverse_lazy('blog_note:list')

    def form_valid(self, form):
        if form.is_valid():
            new_slug = form.save()
            new_slug.slug = slugify(new_slug.title)
            new_slug.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog_note:view', args=[self.kwargs.get('pk')])


class BlogNoteDeleteView(DeleteView):
    model = Blog_note
    success_url = reverse_lazy('blog_note:list')



