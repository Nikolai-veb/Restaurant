from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .forms import CommentsForm
from .models import Categories, Tags, Products, Comments
from cart.forms import CartAddProductForm

class ProductListView(ListView):
    model = Products
    context_object_name = 'product_list'
    template_name = 'shop/product_list.html'
    paginate_by = 10

    def get_queryset(self):
        cat_slug = 'cat_slug'
        tag_slug = 'tag_slug'
        queryset = Products.manager.prefetch_related("tags")
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

    def get_queryset(self):
        queryset = Products.manager.filter(slug=self.kwargs['prod_slug']).select_related('category')
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        context['tags'] = Tags.objects.all()
        context['form'] = CommentsForm()
        context['form_cart'] = CartAddProductForm()
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
