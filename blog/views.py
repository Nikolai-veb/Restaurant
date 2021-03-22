from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Recipes, Tags, Categories
from .forms import CommentsForm


class RecipeListView(ListView):
    model = Recipes
    context_object_name = 'recipes'
    template_name = 'blog/recipe_list.html'
    paginate_by = 10

    def get_queryset(self):
        cat_slug = 'cat_slug'
        tag_slug = 'tag_slug'
        queryset = Recipes.manager.prefetch_related("tags")
        if cat_slug in self.kwargs:
            queryset = Recipes.manager.filter(category__slug=self.kwargs['cat_slug'])
        elif tag_slug in self.kwargs:
            queryset = Recipes.manager.filter(tags__slug=self.kwargs['tag_slug'])
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        context['tags'] = Tags.objects.all()
        context['recent_recipe'] = Recipes.objects.filter(moderation=True)[:2]
        return context


class RecipeDetailView(DetailView):
    model = Recipes
    context_object_name = 'recipe'
    template_name = 'blog/recipe_detail.html'
    slug_url_kwarg = 'rec_slug'

    def get_queryset(self):
        queryset = Recipes.manager.filter(slug=self.kwargs['rec_slug']).select_related('category')
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        context['tags'] = Tags.objects.all()
        context['recent_recipe'] = Recipes.objects.filter(moderation=True)[:2]
        context['form'] = CommentsForm()
        return context


class AddComment(View):
    def post(self, request, pk):
        recipe = Recipes.objects.get(id=pk, moderation=True)
        form = CommentsForm(self.request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if self.request.POST.get("parent", None):
                form.parent_id = (self.request.POST.get("parent"))
            form.recipe = recipe
            form.save()
        return redirect(recipe.get_absolute_url())
