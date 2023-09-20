from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    extra_context = {
        'title': 'Главная',
    }

def contacts(request):
    context = {
        'title': 'Контакты'
    }
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone}: {message}')
    return render(request, 'catalog/contacts.html', context)



def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object_list':  Product.objects.filter(pk=pk),
        'title': product_item.name,
    }
    return render(request, 'catalog/product.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/home.html'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['pk'] = product_item.pk
        context_data['title'] = product_item.name
        return context_data