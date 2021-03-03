from django.shortcuts import render
from django.views.generic import ListView
from .models import Categories, Status, Products


def home_page(request):
    menu = Products.objects.all()
    return render(request, 'home_page.html', {menu: 'menu'})

class MenuListView(ListView):
    model = Products
    context_object_name = 'list_menu'
    template_name = 'menu/list_menu.html'