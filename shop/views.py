from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .forms import CommentsForm
from .models import Categories, Tags, Products, Comments


class ProductListView(ListView):
    model = Products
    context_object_name = 'list_products'
    template_name = 'shop/product_list.html'
    queryset = Products.objects.filter(moderation=True).select_related("category", "tags")

    def get_queryset(self):
        cat_slug = 'cat_slug'
        tag_slug = 'tag_slug'
        queryset = Products.manager.select_related("category")
        if cat_slug in self.kwargs:
            queryset = Products.manager.filter(category__slug=self.kwargs['cat_slug'])
        elif tag_slug in self.kwargs:
            queryset = Products.manager.filter(tags__slug=self.kwargs['tag_slug'])
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        context['tags'] = Tags.objects.all()
        context['recent_product'] = Products.objects.filter(moderation=True)[:2]
        return context


class ProductDetailView(DetailView):
    model = Products
    context_object_name = 'product'
    template_name = 'shop/product_detail.html'
    slug_url_kwarg = 'prod_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        context['tags'] = Tags.objects.all()
        context['recent_product'] = Products.objects.filter(moderation=True)[:2]
        context['form'] = CommentsForm()
        return context


class AddComment(View):
    def post(self, request, pk):
        product = Products.objects.get(id=pk, moderation=True)
        form = CommentsForm(self.request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if self.request.POST.get("parent", None):
                form.parent_id = (self.request.POST.get("parent"))
            form.product = product
            form.save()
        return redirect(product.get_absolute_url())
