from django.shortcuts import render
from django.views.generic import ListView
from .models import Categories, Status, Products


def home_page(request):
    categories = Categories.objects.all()
    products = Products.objects.filter(moderation=True)
    return render(request, 'home_page.html', {'products': products, 'categories': categories})


class MenuListView(ListView):
    model = Products
    context_object_name = 'list_menu'
    template_name = 'menu/list_menu.html'
    queryset = Products.objects.filter(moderation=True).select_related("category", "status")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        return context