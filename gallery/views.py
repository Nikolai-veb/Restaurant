from django.shortcuts import render
from django.views.generic import ListView

from .models import Categories, Images


class GalleryListView(ListView):
    model = Images
    context_object_name = 'images'
    template_name = 'gallery/gallery_grid.html'
    queryset = Images.objects.filter(moderation=True).select_related("category")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        return context
